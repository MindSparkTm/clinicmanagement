# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0009_auto_20180309_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sent_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
