# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-06 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_memberinfosanlamdatabase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member_info',
            options={},
        ),
        migrations.RemoveField(
            model_name='member_info',
            name='created',
        ),
        migrations.RemoveField(
            model_name='member_info',
            name='last_updated',
        ),
        migrations.AlterField(
            model_name='member_info',
            name='cancelled',
            field=models.CharField(max_length=10),
        ),
    ]