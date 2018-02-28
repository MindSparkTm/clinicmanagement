# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 12:09
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabResults',
            fields=[
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='patient_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('labresult_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('triage_id', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_no', models.TextField(max_length=100)),
                ('tests_done', models.TextField(blank=True, max_length=400, null=True)),
                ('test_results', models.TextField(max_length=400)),
                ('uploaded_file', models.FileField(blank=True, null=True, upload_to='media/lab/')),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='lab_name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('lab_name', models.TextField(blank=True, max_length=100, null=True)),
                ('lab_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('triage_id', models.CharField(blank=True, max_length=100, null=True)),
                ('h01', models.BooleanField(default=False)),
                ('h02', models.BooleanField(default=False)),
                ('h03', models.BooleanField(default=False)),
                ('h04', models.BooleanField(default=False)),
                ('h05', models.BooleanField(default=False)),
                ('h06', models.BooleanField(default=False)),
                ('h07', models.BooleanField(default=False)),
                ('h08', models.BooleanField(default=False)),
                ('h09', models.BooleanField(default=False)),
                ('c01', models.BooleanField(default=False)),
                ('c02', models.BooleanField(default=False)),
                ('p01', models.BooleanField(default=False)),
                ('p02', models.BooleanField(default=False, max_length=100)),
                ('p03', models.BooleanField(default=False)),
                ('p04', models.BooleanField(default=False)),
                ('p05', models.BooleanField(default=False)),
                ('p06', models.BooleanField(default=False)),
                ('mbs01', models.BooleanField(default=False)),
                ('mbs02', models.BooleanField(default=False)),
                ('mbs03', models.BooleanField(default=False)),
                ('ge01', models.BooleanField(default=False)),
                ('lks01', models.BooleanField(default=False)),
                ('lks02', models.BooleanField(default=False)),
                ('lks03', models.BooleanField(default=False)),
                ('lks04', models.BooleanField(default=False)),
                ('lks05', models.BooleanField(default=False)),
                ('lks06', models.BooleanField(default=False)),
                ('lks07', models.BooleanField(default=False)),
                ('gm01', models.BooleanField(default=False)),
                ('gm02', models.BooleanField(default=False)),
                ('gm03', models.BooleanField(default=False)),
                ('lm01', models.BooleanField(default=False)),
                ('lm02', models.BooleanField(default=False)),
                ('lm03', models.BooleanField(default=False)),
                ('lm04', models.BooleanField(default=False)),
                ('lpg01', models.BooleanField(default=False)),
                ('lpg02', models.BooleanField(default=False)),
                ('lpg03', models.BooleanField(default=False, max_length=100)),
                ('lpg04', models.BooleanField(default=False)),
                ('lpg05', models.BooleanField(default=False)),
                ('lpg06', models.BooleanField(default=False)),
                ('lpg07', models.BooleanField(default=False)),
                ('lpg08', models.BooleanField(default=False)),
                ('hv01', models.BooleanField(default=False)),
                ('hv02', models.BooleanField(default=False)),
                ('hv03', models.BooleanField(default=False)),
                ('i01', models.BooleanField(default=False)),
                ('i02', models.BooleanField(default=False)),
                ('i03', models.BooleanField(default=False)),
                ('m01', models.BooleanField(default=False)),
                ('m02', models.BooleanField(default=False)),
                ('m03', models.BooleanField(default=False)),
                ('M04', models.BooleanField(default=False)),
                ('m05', models.BooleanField(default=False)),
                ('m06', models.BooleanField(default=False)),
                ('m07', models.BooleanField(default=False)),
                ('m08', models.BooleanField(default=False)),
                ('g01', models.BooleanField(default=False, max_length=200)),
                ('other', models.TextField(blank=True, max_length=100, null=True)),
                ('diagnosis', models.TextField(blank=True, max_length=100, null=True)),
                ('h01_alergy', models.BooleanField(default=False)),
                ('h02_alergy', models.BooleanField(default=False)),
                ('h03_alergy', models.BooleanField(default=False)),
                ('h04_alergy', models.BooleanField(default=False)),
                ('h06_alergy', models.BooleanField(default=False)),
                ('h07_alergy', models.BooleanField(default=False)),
                ('h08_alergy', models.BooleanField(default=False, max_length=100)),
                ('c01_iron_studies', models.BooleanField(default=False)),
                ('c01_cardiac_markers', models.BooleanField(default=False, max_length=100)),
                ('c02_cardiac_markers', models.BooleanField(default=False, max_length=100)),
                ('c02_cardiac_markers_1', models.BooleanField(default=False, max_length=100)),
                ('lks01_antenatal_screen', models.BooleanField(default=False)),
                ('lks02_antenatal_screen', models.BooleanField(default=False, max_length=100)),
                ('lks04_antenatal_screen', models.BooleanField(default=False, max_length=100)),
                ('lks05_antenatal_screen', models.BooleanField(default=False, max_length=100)),
                ('lks06_antenatal_screen', models.BooleanField(default=False, max_length=100)),
                ('lks07_antenatal_screen', models.BooleanField(default=False, max_length=100)),
                ('gm01_antenatal_screen', models.BooleanField(default=False)),
                ('fsh_menopausal_screen', models.BooleanField(default=False)),
                ('oestradiol_menopausal_screen', models.BooleanField(default=False, max_length=100)),
                ('albumin_menopausal_screen', models.BooleanField(default=False)),
                ('hv02_menopausal_screen', models.BooleanField(default=False, max_length=100)),
                ('hv03_menopausal_screen', models.BooleanField(default=False)),
                ('ast_menopausal_screen', models.BooleanField(default=False, max_length=100)),
                ('i01_menopausal_screen', models.BooleanField(default=False, max_length=100)),
                ('i02_menopausal_screen', models.BooleanField(default=False)),
                ('i03_menopausal_screen', models.TextField(blank=True, max_length=100, null=True)),
                ('patient_no', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='Radiology',
            fields=[
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='patient_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('radiology_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('triage_id', models.CharField(blank=True, max_length=100, null=True)),
                ('lpm_date', models.BooleanField(default=False)),
                ('could_b_pregrant', models.TextField(blank=True, max_length=100, null=True)),
                ('examination', models.TextField(blank=True, max_length=200, null=True)),
                ('clinical_indication', models.TextField(blank=True, max_length=200, null=True)),
                ('intra_orbital_fb_hist', models.BooleanField(default=False)),
                ('intracranial_clip', models.BooleanField(default=False)),
                ('pacemaker', models.BooleanField(default=False)),
                ('cochlear_implants', models.BooleanField(default=False)),
                ('prosthetic_hrt_valve', models.BooleanField(default=False)),
                ('pregnancy', models.BooleanField(default=False)),
                ('recent_surgery', models.BooleanField(default=False)),
                ('patient_info', models.BooleanField(default=False)),
                ('diabetic_metformin', models.BooleanField(default=False)),
                ('allergic_contrast', models.BooleanField(default=False)),
                ('other_allergies', models.BooleanField(default=False, max_length=100)),
                ('kidney_problems', models.BooleanField(default=False)),
                ('anticoagulant_drugs', models.BooleanField(default=False)),
                ('egfr_result', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('patient_no', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='RadiologyResult',
            fields=[
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='patient_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('patient_no', models.CharField(max_length=30)),
                ('results', models.TextField(max_length=400)),
                ('radiologyresult_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('triage_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tests_done', models.TextField(blank=True, max_length=400, null=True)),
                ('uploaded_file', models.FileField(blank=True, null=True, upload_to='media/radiology/')),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
    ]
