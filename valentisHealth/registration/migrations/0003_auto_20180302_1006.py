# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20180301_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='alt_phone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='primary_insurance',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]