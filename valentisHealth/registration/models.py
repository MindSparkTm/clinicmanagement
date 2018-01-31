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

    #history
    occupation = models.CharField(max_length=30, null="True", blank="True")
    marital_status = models.CharField(max_length=30, null="True", blank="True")
    spouse = models.CharField(max_length=30, null="True", blank="True")
    no_children = models.IntegerField(null="True", blank="True")
    childrens = models.CharField(max_length=100, null="True", blank="True")
    prev_docs = models.CharField(max_length=200, null="True", blank="True")
    medical_information = models.TextField(max_length=1000, null="True", blank="True")
    alergies = models.TextField(max_length=1000, null="True", blank="True")
    preferred_pharmacy = models.TextField(max_length=100, null="True", blank="True")
    last_phys_examination = models.DateField(null="True", blank="True")
    last_blood_work = models.DateField(null="True", blank="True")
    last_colonoscopy = models.DateField(null="True", blank="True")
    last_tetanus_shot = models.DateField(null="True", blank="True")
    last_menstrual = models.DateField(null="True", blank="True")
    last_pap_smear = models.DateField(null="True", blank="True")
    last_mammogram = models.DateField(null="True", blank="True")
    dexa = models.TextField(max_length=100, null="True", blank="True")
    no_pregnancies = models.IntegerField(null="True", blank="True")
    miscourages = models.TextField(max_length=100, null="True", blank="True")
    living_children = models.CharField(max_length=30, null="True", blank="True")
    methods_of_contraception = models.TextField(max_length=100, null="True", blank="True")
    surgeries = models.TextField(max_length=1000, null="True", blank="True")
    genetic_diseases = models.TextField(max_length=1000, null="True", blank="True")
    if_smoker = models.CharField(max_length=30, null="True", blank="True")
    cigar_per_day = models.CharField(max_length=30, null="True", blank="True")
    no_of_yr_smoking = models.CharField(max_length=30, null="True", blank="True")
    if_chew_tobacco = models.CharField(max_length=30, null="True", blank="True")
    yrs_chewing_tobacco = models.CharField(max_length=30, null="True", blank="True")
    if_quit_before = models.CharField(max_length=30, null="True", blank="True")
    tobacco_quit_duration = models.CharField(max_length=30, null="True", blank="True")
    if_drink_alcohol = models.CharField(max_length=30, null="True", blank="True")
    alocohol_type = models.CharField(max_length=30, null="True", blank="True")
    alcohol_frequency = models.CharField(max_length=30, null="True", blank="True")
    if_drug_used = models.CharField(max_length=30, null="True", blank="True")
    drug_type = models.TextField(max_length=100, null="True", blank="True")
    when_drug_used = models.CharField(max_length=30, null="True", blank="True")
    if_exercise = models.CharField(max_length=30, null="True", blank="True")
    exercise_freq = models.CharField(max_length=30, null="True", blank="True")
    if_special_diet = models.CharField(max_length=30, null="True", blank="True")
    special_diet = models.TextField(max_length=100, null="True", blank="True")
    if_use_caffein = models.CharField(max_length=30, null="True", blank="True")
    caffein_daily_amt = models.CharField(max_length=30, null="True", blank="True")
    is_sadder = models.CharField(max_length=30, null="True", blank="True")
    if_lost_interest = models.CharField(max_length=30, null="True", blank="True")
    have_will = models.CharField(max_length=30, null="True", blank="True")

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('registration_models_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('registration_models_update', args=(self.pk,))


