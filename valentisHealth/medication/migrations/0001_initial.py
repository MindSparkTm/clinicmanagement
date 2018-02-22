
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
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='patient_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('prescription_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('triage_id', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('patient_no', models.CharField(max_length=30)),
                ('patient_name', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('phone_number', models.CharField(max_length=30)),
                ('signature', models.BinaryField(blank=True, null=True)),
                ('prescription', models.TextField(max_length=400)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='MyDawa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ('brand',),
            },
        ),
    ]
