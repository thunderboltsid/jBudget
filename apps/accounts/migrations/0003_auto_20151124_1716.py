# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151018_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(max_length=15, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'x', b'Other')]),
        ),
    ]
