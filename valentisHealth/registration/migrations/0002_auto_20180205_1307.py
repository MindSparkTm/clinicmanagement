# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-05 10:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='models',
            old_name='Gender',
            new_name='gender',
        ),
    ]
