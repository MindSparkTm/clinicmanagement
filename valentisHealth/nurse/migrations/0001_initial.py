
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
            name='models',
            fields=[
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='patient_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('triage_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('systolic', models.IntegerField()),
                ('diastolic', models.IntegerField()),
                ('temperature', models.FloatField()),
                ('oxygen_saturation', models.FloatField()),
                ('urinalysis', models.TextField(blank=True, max_length=400, null=True)),
                ('random_glucose', models.TextField(blank=True, max_length=400, null=True)),
                ('heart_rate', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('others', models.TextField(blank=True, max_length=200, null=True)),
                ('attending_nurse', models.CharField(blank=True, max_length=30, null=True)),
                ('patient_no', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'ordering': ('-last_updated',),
            },
        ),
    ]
