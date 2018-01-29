from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
import datetime



class member_info(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='member_no', blank=True)
    family_no = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    member_no = models.CharField(max_length=20)
    surname = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    other_name = models.CharField(max_length=40)
    dob = models.DateField(default=datetime.date.today)
    user_id = models.CharField(max_length=10)
    date_entered = models.DateField(default=datetime.date.today)
    cancelled = models.DecimalField(max_digits=1,decimal_places=0)
    employment_no = models.CharField(max_length=20)
    gender = models.DecimalField(max_digits=1,decimal_places=0)
    passport_no = models.CharField(max_length=15)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.surname)

    def get_absolute_url(self):
        return reverse('payments_member_info_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('payments_member_info_update', args=(self.slug,))

    def get_status(self):
        pass


class member_benefits(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='member_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    member_no = models.CharField(max_length=20)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    sharing = models.DecimalField(max_digits=1, decimal_places=0)
    anniv = models.DecimalField(max_digits=2, decimal_places=0)
    suspended = models.DecimalField(max_digits=1, decimal_places=0)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    idx = models.DecimalField(max_digits=10, decimal_places=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('payments_member_benefits_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('payments_member_benefits_update', args=(self.slug,))


class member_anniversary(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='member_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    member_no = models.CharField(max_length=20)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    anniv = models.IntegerField()


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('payments_member_anniversary_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('payments_member_anniversary_update', args=(self.slug,))


class member_acceptance(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='member_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    member_no = models.CharField(max_length=20)
    status = models.DecimalField(max_digits=1, decimal_places=0)
    status_date = models.DateField(default=datetime.date.today)
    user_id = models.CharField(max_length=10)
    date_entered = models.DateField(default=datetime.date.today)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('payments_member_acceptance_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('payments_member_acceptance_update', args=(self.slug,))


class principal_applicant(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    family_no = models.CharField(max_length=20, null=False, blank=False)
    first_name = models.CharField(max_length=40)
    postal_add = models.CharField(max_length=15)
    town = models.DecimalField(max_digits=5, decimal_places=0)
    email = models.EmailField()
    other_names = models.CharField(max_length=40)
    corp_id = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=20)
    family_size = models.DecimalField(max_digits=2, decimal_places=0)
    user_id = models.CharField(max_length=10)
    category = models.CharField(max_length=10)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('payments_principal_applicant_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('payments_principal_applicant_update', args=(self.slug,))


class pre_authorization(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='member_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    member_no = models.CharField(max_length=15)

    provider = models.DecimalField(max_digits=5, decimal_places=0)
    date_reported = models.DateField(default=datetime.date.today)
    reported_by = models.CharField(max_length=20)
    authorized_by = models.CharField(max_length=10)
    date_authorized = models.DateField(default=datetime.date.today)
    pre_diagnosis = models.CharField(max_length=60)
    authority_type = models.DecimalField(max_digits=3, decimal_places=0)
    ward = models.DecimalField(max_digits=2, decimal_places=0)
    available_limit = models.DecimalField(max_digits=10, decimal_places=2)
    admit_days = models.DecimalField(max_digits=3, decimal_places=0)
    reserve = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=200)
    anniv = models.DecimalField(max_digits=5, decimal_places=0)
    # auth_batch_no = models.DecimalField(populate_from='code')
    day_bed_charge = models.DecimalField(max_digits=10, decimal_places=2)
    date_admitted = models.DateField(default=datetime.date.today)
    code = models.AutoField(primary_key=True)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('payments_pre_authorization_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('payments_pre_authorization_update', args=(self.slug,))


class provider(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    code = models.CharField(max_length=10)
    provider = models.CharField(max_length=60)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('payments_provider_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('payments_provider_update', args=(self.slug,))


class cash(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    items = models.TextField(max_length=400)
    amount_payed = models.DecimalField(max_digits=1,decimal_places=0)
    total_cost = models.FloatField(max_length=10)
    balance = models.TextField(max_length=100)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('payments_cash_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('payments_cash_update', args=(self.slug,))


