import re

from django.db import models
from django.utils.translation import gettext_lazy as _

from M2Crypto import X509


class Identity(models.Model):
    certificate = models.TextField(
        help_text=_('A PEM-encoded X.509 certificate.')
    )

    address = models.EmailField(
        blank=True,
        max_length=256,
        help_text=_('If left blank, it will be extracted from the X.509 certificate.')
    )

    key = models.TextField(
        blank=True,
        help_text=_('If mail <em>from</em> this identity should be signed, put a PEM-encoded private key here. Make sure it does not require a passphrase.')
    )

    not_before = models.DateField(
        blank=True,
        help_text=_('If left blank, it will be extracted from the X.509 certificate.')
    )

    not_after = models.DateField(
        blank=True,
        help_text=_('If left blank, it will be extracted from the X.509 certificate.')
    )

    class Meta:
        ordering = ['address']
        verbose_name_plural = _('Identities')

    def __unicode__(self):
        return self.address or self

    @property
    def fingerprint(self):
        fingerprint = self.x509.get_fingerprint(md='sha1').rjust(40, '0')
        return re.sub(r'(..)(?!$)', r'\1:', fingerprint)

    @property
    def x509(self):
        return X509.load_cert_string(str(self.certificate))


def set_identity_fields_from_certificate(sender, **kwargs):
    identity = kwargs['instance']
    if not identity.address or not identity.not_before or not identity.not_after:
        x509 = identity.x509

        if not identity.address:
            subject = x509.get_subject()
            email_address = subject.get_entries_by_nid(subject.nid['emailAddress'])[0]
            identity.address = str(email_address.get_data())

        if not identity.not_before:
            identity.not_before = x509.get_not_before().get_datetime()

        if not identity.not_after:
            identity.not_after = x509.get_not_after().get_datetime()

models.signals.pre_save.connect(set_identity_fields_from_certificate, sender=Identity)
