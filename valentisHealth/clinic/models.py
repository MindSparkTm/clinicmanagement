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


class patientVisit(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    patient_id = models.CharField(max_length=30)
    visit_id = models.CharField(max_length=30)
    radiology_no = models.CharField(max_length=30, null=True, blank=True)
    notes = models.TextField(max_length=200, null=True, blank=True)
    diagnosis = models.TextField(max_length=100, null=True, blank=True)
    prescription_id = models.CharField(max_length=30, null=True, blank=True)
    status = models.IntegerField(max_length=2)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('clinic_patientvisit_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('clinic_patientvisit_update', args=(self.slug,))


