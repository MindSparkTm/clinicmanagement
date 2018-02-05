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


class pre_auth(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    reference_no = models.TextField(max_length=100)
    authority_type = models.TextField(max_length=100)
    provider = models.TextField(max_length=100)
    ward = models.TextField(max_length=100)
    date_admitted = models.TextField(max_length=100)
    date_provided = models.TextField(max_length=100)
    notes = models.TextField(max_length=100)
    claim = models.TextField(max_length=100)
    limit = models.TextField(max_length=100)
    batch_no = models.CharField(max_length=30)
    date_reported = models.TextField(max_length=100)
    admit_days = models.IntegerField()
    anniv = models.IntegerField()
    daily_bed_limit = models.FloatField()
    type = models.CharField(max_length=30)
    authorised_by = models.TextField(max_length=100)


    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('pre_auth_pre_auth_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('pre_auth_pre_auth_update', args=(self.slug,))


