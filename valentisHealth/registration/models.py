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
    patient_id = models.AutoField(primary_key=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    first_name = CharField(max_length=30)
    middle_name = CharField(max_length=30, null=True, blank=True)
    last_name = CharField(max_length=30)
    Gender = CharField(max_length=30)
    street_name = CharField(max_length=30, null=True, blank=True)
    apartment_name = CharField(max_length=30, null=True, blank=True)
    postal_code = CharField(max_length=30, null=True, blank=True)
    postal_address = TextField(max_length=100,null=True, blank=True)
    city = CharField(max_length=30,null=True, blank=True)
    country = CharField(max_length=30,null=True, blank=True)
    age = IntegerField(null=True, blank=True)
    next_of_kin = TextField(max_length=100,null=True, blank=True)
    n_of_kin_rel = TextField(max_length=100,null=True, blank=True)
    email = EmailField(null=True, blank=True)
    phone = IntegerField(null=True, blank=True)
    primary_insurance = TextField(max_length=10, null=True, blank=True)
    secondary_insurance = TextField(max_length=100, null=True, blank=True)
    pri_ins_sub = models.DecimalField(max_digits=1,decimal_places=0, null=True, blank=True)
    sec_ins_sub = models.DecimalField(max_digits=1,decimal_places=0, null=True, blank=True)
    other_ins_subscriber = TextField(max_length=100, null=True, blank=True)
    subscriber_relationship = TextField(max_length=100, null=True, blank=True)
    sub_address = TextField(max_length=100, null=True, blank=True)
    ss_number = TextField(max_length=100, null=True, blank=True)
    sub_ss_number = TextField(max_length=100,null=True, blank=True)
    alt_phone = IntegerField(null=True, blank=True)
    sub_work_phone = TextField(max_length=100, null=True, blank=True)
    dob = DateField(null=True, blank=True)
    sub_dob = DateField(null=True, blank=True)
    sub_employer = TextField(max_length=100,null=True, blank=True)
    status = IntegerField(null=True, blank=True)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('registration_models_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('registration_models_update', args=(self.pk,))


