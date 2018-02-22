
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('items', models.TextField(max_length=400)),
                ('amount_payed', models.DecimalField(decimal_places=0, max_digits=1)),
                ('total_cost', models.FloatField(max_length=10)),
                ('balance', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='member_acceptance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='member_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('member_no', models.CharField(max_length=20)),
                ('status', models.DecimalField(decimal_places=0, max_digits=1)),
                ('status_date', models.DateField(default=datetime.date.today)),
                ('user_id', models.CharField(max_length=10)),
                ('date_entered', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='member_anniversary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='member_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('member_no', models.CharField(max_length=20)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('anniv', models.IntegerField()),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='member_benefits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='member_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('member_no', models.CharField(max_length=20)),
                ('limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sharing', models.DecimalField(decimal_places=0, max_digits=1)),
                ('anniv', models.DecimalField(decimal_places=0, max_digits=2)),
                ('suspended', models.DecimalField(decimal_places=0, max_digits=1)),
                ('suspended_date', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('expense', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idx', models.DecimalField(decimal_places=0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='member_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='member_no')),
                ('family_no', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('member_no', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=40)),
                ('other_name', models.CharField(max_length=40)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('user_id', models.CharField(max_length=10)),
                ('date_entered', models.DateField(default=datetime.date.today)),
                ('cancelled', models.DecimalField(decimal_places=0, max_digits=1)),
                ('employment_no', models.CharField(max_length=20)),
                ('gender', models.DecimalField(decimal_places=0, max_digits=1)),
                ('passport_no', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='pre_authorization',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='member_no')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('member_no', models.CharField(max_length=15)),
                ('provider', models.IntegerField(choices=[(0, 'AGA KHAN HOSPITAL NAIROBI'), (1, 'NAIROBI HOSPITAL'), (2, 'KENYATTA HOSPITAL'), (3, 'KAREN HOSPITAL')], default=0)),
                ('date_reported', models.DateField(default=datetime.date.today)),
                ('reported_by', models.CharField(max_length=20)),
                ('authorized_by', models.CharField(max_length=10)),
                ('date_authorized', models.DateField(default=datetime.date.today)),
                ('pre_diagnosis', models.CharField(max_length=60)),
                ('authority_type', models.IntegerField(choices=[(0, 'In Patient'), (1, 'Out Patient'), (3, 'Dental'), (4, 'Maternity')], default=0)),
                ('ward', models.IntegerField(choices=[(0, 'General Ward'), (1, 'Maternity Ward'), (2, 'Children Ward'), (3, 'Critical Ward')], default=0)),
                ('available_limit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('admit_days', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('reserve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.CharField(max_length=200)),
                ('internal_notes', models.CharField(choices=[('EXT', 'Ext'), ('NEW', 'New')], default='NEW', max_length=100)),
                ('anniv', models.DecimalField(decimal_places=0, max_digits=5, null=True)),
                ('day_bed_charge', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_admitted', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('code', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='principal_applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('family_no', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=40)),
                ('postal_add', models.CharField(max_length=15)),
                ('town', models.DecimalField(decimal_places=0, max_digits=5)),
                ('email', models.EmailField(max_length=254)),
                ('other_names', models.CharField(max_length=40)),
                ('corp_id', models.CharField(max_length=10)),
                ('mobile_no', models.CharField(max_length=20)),
                ('family_size', models.DecimalField(decimal_places=0, max_digits=2)),
                ('user_id', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=10)),
                ('provider', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ('last_updated',),
            },
        ),
    ]
