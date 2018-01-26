from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class models(models.Model):

    # Fields
    patient_id = CharField(max_length=200, unique=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    first_name = CharField(max_length=30)
    middle_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    Gender = CharField(max_length=30)
    street_name = CharField(max_length=30)
    apartment_name = CharField(max_length=30)
    postal_code = CharField(max_length=30)
    postal_address = TextField(max_length=100)
    city = CharField(max_length=30)
    country = CharField(max_length=30)
    age = IntegerField()
    next_of_kin = TextField(max_length=100)
    n_of_kin_rel = TextField(max_length=100)
    email = EmailField()
    phone = IntegerField()
    primary_insurance = TextField(max_length=100)
    secondary_insurance = TextField(max_length=100)
    pri_ins_sub = BooleanField(max_length=100)
    sec_ins_sub = BooleanField()
    other_ins_subscriber = TextField(max_length=100)
    subscriber_relationship = TextField(max_length=100)
    sub_address = TextField(max_length=100)
    ss_number = TextField(max_length=100)
    sub_ss_number = TextField(max_length=100)
    alt_phone = IntegerField()
    sub_work_phone = TextField(max_length=100)
    dob = DateField(null=True, blank=True)
    sub_dob = DateField(null=True, blank=True)
    sub_employer = TextField(max_length=100)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('registration_models_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('registration_models_update', args=(self.pk,))


