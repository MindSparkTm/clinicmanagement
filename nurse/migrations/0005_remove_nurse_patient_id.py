# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-03 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nurse', '0004_auto_20180403_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='patient_id',
        ),
    ]
