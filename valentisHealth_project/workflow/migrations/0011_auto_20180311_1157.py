# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 08:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0010_auto_20180309_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages+', to=settings.AUTH_USER_MODEL, verbose_name='recipient'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages+', to=settings.AUTH_USER_MODEL, verbose_name='sender'),
        ),
    ]
