# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-23 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0004_auto_20180319_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='pharmacy',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]