# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-16 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20180316_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='e_contact_address',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='e_phone_number',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='e_relationship',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='emergency_contact',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
