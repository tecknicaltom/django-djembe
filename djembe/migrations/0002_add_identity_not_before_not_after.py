# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
    ]
