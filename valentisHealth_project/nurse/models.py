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
import uuid

class models(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no',null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    triage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    systolic = models.IntegerField()
    diastolic = models.IntegerField()
    temperature = models.FloatField()
    oxygen_saturation = models.FloatField()
    urinalysis = models.TextField(max_length=400, null=True, blank=True)
    random_glucose = models.TextField(max_length=400, null=True, blank=True)
    heart_rate = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    others = models.TextField(max_length=200, null=True, blank=True)
    attending_nurse = models.CharField(max_length=255, null=True, blank=True)
    patient_no = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('nurse_models_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('nurse_models_update', args=(self.slug,))