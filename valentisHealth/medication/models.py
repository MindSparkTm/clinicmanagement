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
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    prescription_id = models.CharField(max_length=30)
    patients_id = models.CharField(max_length=30)
    patient_name = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    phone_number = models.IntegerField()
    signature = models.BinaryField()
    prescription = models.TextField(max_length=400)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('medication_models_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('medication_models_update', args=(self.slug,))


