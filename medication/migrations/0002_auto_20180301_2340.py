# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='triage_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]