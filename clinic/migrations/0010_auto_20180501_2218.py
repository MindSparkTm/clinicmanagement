# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-01 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0009_patientvisit_current_diagnosis'),
    ]

    operations = [
        migrations.CreateModel(
            name='RadiologyTestsresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radiologytestid', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('resulturl', models.CharField(blank=True, max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Testsresults',
            new_name='LabTestsresults',
        ),
        migrations.RenameField(
            model_name='labtestsresults',
            old_name='testid',
            new_name='labtestid',
        ),
    ]
