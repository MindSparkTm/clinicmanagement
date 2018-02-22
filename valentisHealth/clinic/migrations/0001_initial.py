
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
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='patientVisit',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='patient_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('patient_no', models.CharField(blank=True, max_length=30, null=True)),
                ('visit_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('radiology_no', models.CharField(blank=True, max_length=30, null=True)),
                ('triage_id', models.CharField(blank=True, max_length=30, null=True)),
                ('notes', models.TextField(blank=True, max_length=200, null=True)),
                ('diagnosis', models.TextField(blank=True, max_length=100, null=True)),
                ('prescription_id', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
    ]
