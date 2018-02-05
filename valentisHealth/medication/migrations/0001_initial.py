# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-02 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='models',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='patient_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('prescription_id', models.CharField(blank=True, max_length=30, null=True)),
                ('patient_no', models.CharField(max_length=30)),
                ('patient_name', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('signature', models.BinaryField(default=True)),
                ('prescription', models.TextField(max_length=400)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
    ]
