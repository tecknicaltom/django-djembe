# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

from M2Crypto import X509


def generate_dates(apps, schema_editor):
    Identity = apps.get_model("djembe", "Identity")
    for identity in Identity.objects.all():
        x509 = X509.load_cert_string(str(identity.certificate))
        identity.not_before = x509.get_not_before().get_datetime()
        identity.not_after = x509.get_not_after().get_datetime()
        identity.save()

class Migration(migrations.Migration):

    dependencies = [
        ('djembe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='identity',
            name='not_after',
            field=models.DateField(help_text='If left blank, it will be extracted from the X.509 certificate.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='identity',
            name='not_before',
            field=models.DateField(help_text='If left blank, it will be extracted from the X.509 certificate.', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RunPython(generate_dates),
        migrations.AlterField(
            model_name='identity',
            name='not_after',
            field=models.DateField(help_text='If left blank, it will be extracted from the X.509 certificate.', blank=True),
        ),
        migrations.AlterField(
            model_name='identity',
            name='not_before',
            field=models.DateField(help_text='If left blank, it will be extracted from the X.509 certificate.', blank=True),
        ),
    ]
