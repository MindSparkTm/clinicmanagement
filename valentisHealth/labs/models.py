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


class labs(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    lab_name = models.TextField(max_length=100)
    h01 = models.BooleanField()
    h02 = models.BooleanField()
    h03 = models.BooleanField()
    h04 = models.BooleanField()
    h05 = models.BooleanField()
    h06 = models.BooleanField()
    h07 = models.BooleanField()
    h08 = models.BooleanField()
    h09 = models.BooleanField()
    c01 = models.BooleanField()
    c02 = models.BooleanField()
    p01 = models.BooleanField()
    p02 = models.BooleanField(max_length=100)
    p03 = models.BooleanField()
    p04 = models.BooleanField()
    p05 = models.BooleanField()
    p06 = models.BooleanField()
    mbs01 = models.BooleanField()
    mbs02 = models.BooleanField()
    mbs03 = models.BooleanField()
    ge01 = models.BooleanField()
    lks01 = models.BooleanField()
    lks02 = models.BooleanField()
    lks03 = models.BooleanField()
    lks04 = models.BooleanField()
    lks05 = models.BooleanField()
    lks06 = models.BooleanField()
    lks07 = models.BooleanField()
    gm01 = models.BooleanField()
    gm02 = models.BooleanField()
    gm03 = models.BooleanField()
    lm01 = models.BooleanField()
    lm02 = models.BooleanField()
    lm03 = models.BooleanField()
    lm04 = models.BooleanField()
    lpg01 = models.BooleanField()
    lpg02 = models.BooleanField()
    lpg03 = models.BooleanField(max_length=100)
    lpg04 = models.BooleanField()
    lpg05 = models.BooleanField()
    lpg06 = models.BooleanField()
    lpg06 = models.BooleanField()
    lpg07 = models.BooleanField()
    lpg08 = models.BooleanField()
    hv01 = models.BooleanField()
    hv02 = models.BooleanField()
    hv03 = models.BooleanField()
    i01 = models.BooleanField()
    i02 = models.BooleanField()
    i03 = models.BooleanField()
    m01 = models.BooleanField()
    m02 = models.BooleanField()
    m03 = models.BooleanField()
    M04 = models.BooleanField()
    m05 = models.BooleanField()
    m06 = models.BooleanField()
    m07 = models.BooleanField()
    m08 = models.BooleanField()
    g01 = models.BooleanField(max_length=200)
    other = models.TextField(max_length=100)
    diagnosis = models.TextField(max_length=100)
    h01_alergy = models.BooleanField()
    h02_alergy = models.BooleanField()
    h03_alergy = models.BooleanField()
    h04_alergy = models.BooleanField()
    h06_alergy = models.BooleanField()
    h07_alergy = models.BooleanField()
    h08_alergy = models.BooleanField(max_length=100)
    c01_iron_studies = models.BooleanField()
    c01_cardiac_markers = models.BooleanField(max_length=100)
    c02_cardiac_markers = models.BooleanField(max_length=100)
    c02_cardiac_markers_1 = models.BooleanField(max_length=100)
    lks01_antenatal_screen = models.BooleanField()
    lks02_antenatal_screen = models.BooleanField(max_length=100)
    lks04_antenatal_screen = models.BooleanField(max_length=100)
    lks05_antenatal_screen = models.BooleanField(max_length=100)
    lks06_antenatal_screen = models.BooleanField(max_length=100)
    lks07_antenatal_screen = models.BooleanField(max_length=100)
    gm01_antenatal_screen = models.BooleanField()
    fsh_menopausal_screen = models.BooleanField()
    oestradiol_menopausal_screen = models.BooleanField(max_length=100)
    albumin_menopausal_screen = models.BooleanField()
    hv02_menopausal_screen = models.BooleanField(max_length=100)
    hv03_menopausal_screen = models.BooleanField()
    ast_menopausal_screen = models.BooleanField(max_length=100)
    i01_menopausal_screen = models.BooleanField(max_length=100)
    i02_menopausal_screen = models.BooleanField()
    i03_menopausal_screen = models.TextField(max_length=100)
    patient_id = models.CharField(max_length=100)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('labs_labs_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('labs_labs_update', args=(self.slug,))


class radiology(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    lpm_date = models.BooleanField()
    could_b_pregrant = models.TextField(max_length=100)
    examination = models.TextField(max_length=200)
    clinical_indication = models.TextField(max_length=200)
    intra_orbital_fb_hist = models.BooleanField()
    intracranial_clip = models.BooleanField()
    pacemaker = models.BooleanField()
    cochlear_implants = models.BooleanField()
    prosthetic_hrt_valve = models.BooleanField()
    pregnancy = models.BooleanField()
    recent_surgery = models.BooleanField()
    patient_info = models.BooleanField()
    diabetic_metformin = models.BooleanField()
    allergic_contrast = models.BooleanField()
    other_allergies = models.BooleanField(max_length=100)
    kidney_problems = models.BooleanField()
    anticoagulant_drugs = models.BooleanField()
    egfr_result = models.CharField(max_length=30)
    date = models.DateField()
    patient_id = models.CharField(max_length=30)


    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('labs_radiology_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('labs_radiology_update', args=(self.slug,))


