# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-15 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0022_patient_social_allergies'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='child_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]