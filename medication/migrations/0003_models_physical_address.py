# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0002_auto_20180301_2340'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='physical_address',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]