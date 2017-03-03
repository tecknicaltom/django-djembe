# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djembe', '0003_auto_20170303_2159'),
    ]

    operations = [
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
