# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-30 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_auto_20180301_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='radiology',
            name='lab_name',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]