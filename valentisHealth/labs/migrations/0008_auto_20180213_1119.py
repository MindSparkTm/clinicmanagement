# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-13 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0007_auto_20180213_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='labs',
            name='id',
        ),
        migrations.RemoveField(
            model_name='radiology',
            name='id',
        ),
        migrations.AddField(
            model_name='labs',
            name='lab_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='radiology',
            name='radiology_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]