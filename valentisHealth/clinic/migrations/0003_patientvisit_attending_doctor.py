# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_auto_20180301_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientvisit',
            name='attending_doctor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]