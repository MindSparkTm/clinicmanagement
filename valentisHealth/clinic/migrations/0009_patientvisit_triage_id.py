# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-11 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_auto_20180211_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientvisit',
            name='triage_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]