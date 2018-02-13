# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-06 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labresults',
            name='uploaded_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/lab/'),
        ),
        migrations.AddField(
            model_name='radiologyresult',
            name='uploaded_file',
            field=models.FileField(blank=True, null=True, upload_to='documents/radiology/'),
        ),
    ]