from django.urls import reverse
from django.db.models import *
from django.conf import settings
from django.db import models as models
from account.models import CustomUser



class Uploads(models.Model):
    patient_no = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='documents/')

class Patient(models.Model):

    # Fields
    patient_no = models.AutoField(primary_key=True)
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    first_name = CharField(max_length=30)
    middle_name = CharField(max_length=30, null=True, blank=True)
    last_name = CharField(max_length=30)
    gender = CharField(max_length=30)
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
    phone = CharField(max_length=30, null=True, blank=True)
    primary_insurance = TextField(max_length=255, null=True, blank=True)
    secondary_insurance = TextField(max_length=100, null=True, blank=True)
    pri_ins_sub = TextField(max_length=100, null=True, blank=True)
    sec_ins_sub = TextField(max_length=100, null=True, blank=True)
    other_ins_subscriber = TextField(max_length=100, null=True, blank=True)
    subscriber_relationship = TextField(max_length=100, null=True, blank=True)
    sub_address = TextField(max_length=100, null=True, blank=True)
    ss_number = TextField(max_length=100, null=True, blank=True)
    sub_ss_number = TextField(max_length=100,null=True, blank=True)
    alt_phone = CharField(max_length=30, null=True, blank=True)
    sub_work_phone = TextField(max_length=100, null=True, blank=True)
    dob = DateField(null=True, blank=True)
    sub_dob = DateField(null=True, blank=True)
    id_type = TextField(max_length=100, null=True, blank=True)
    sub_id_type=TextField(max_length=100, null=True, blank=True)
    sub_employer = TextField(max_length=100,null=True, blank=True)
    status = IntegerField(null=True, blank=True)
    session_id = TextField(max_length=400, null=True, blank=True)

    uploaded_file = models.FileField(upload_to='media/users/', null=True, blank=True)

    #history
    occupation = models.CharField(max_length=255, default="None", null=True, blank=True)
    marital_status = models.CharField(max_length=255, default="Single", null=True, blank=True)
    spouse = models.CharField(max_length=255, null=True, blank=True)
    no_children = models.IntegerField(null=True, blank=True)
    childrens = models.CharField(max_length=100, null=True, blank=True)
    prev_docs = models.CharField(max_length=200, null=True, blank=True)
    medical_information = models.TextField(max_length=1000, null=True, blank=True)
    alergies = models.TextField(max_length=1000, null=True, blank=True)
    preferred_pharmacy = models.TextField(max_length=100, null=True, blank=True)
    last_phys_examination = models.DateField(null=True, blank=True)
    last_blood_work = models.DateField(null=True, blank=True)
    last_colonoscopy = models.DateField(null=True, blank=True)
    last_tetanus_shot = models.DateField(null=True, blank=True)
    last_menstrual = models.DateField(null=True, blank=True)
    last_pap_smear = models.DateField(null=True, blank=True)
    last_mammogram = models.DateField(null=True, blank=True)
    dexa = models.TextField(max_length=100, null=True, blank=True)
    no_pregnancies = models.IntegerField(null=True, blank=True)
    miscourages = models.TextField(max_length=100, null=True, blank=True)
    living_children = models.CharField(max_length=255, null=True, blank=True)
    methods_of_contraception = models.TextField(max_length=100, null=True, blank=True)
    surgeries = models.TextField(max_length=1000, null=True, blank=True)
    genetic_diseases = models.TextField(max_length=1000, null=True, blank=True)
    if_smoker = models.CharField(max_length=255, default="NO", null=True, blank=True)
    cigar_per_day = models.CharField(max_length=255, null=True, blank=True)
    no_of_yr_smoking = models.CharField(max_length=255, null=True, blank=True)
    if_chew_tobacco = models.CharField(max_length=255, default="NO", null=True, blank=True)
    yrs_chewing_tobacco = models.CharField(max_length=255, null=True, blank=True)
    if_quit_before = models.CharField(max_length=255, default="NO", null=True, blank=True)
    tobacco_quit_duration = models.CharField(max_length=255, null=True, blank=True)
    if_drink_alcohol = models.CharField(max_length=255, default="NO", null=True, blank=True)
    alocohol_type = models.CharField(max_length=255, null=True, blank=True)
    alcohol_frequency = models.CharField(max_length=255, null=True, blank=True)
    if_drug_used = models.CharField(max_length=255, default="NO", null=True, blank=True)
    drug_type = models.TextField(max_length=100, null=True, blank=True)
    when_drug_used = models.CharField(max_length=255, null=True, blank=True)
    if_exercise = models.CharField(max_length=255, default="NO", null=True, blank=True)
    exercise_freq = models.CharField(max_length=255, null=True, blank=True)
    if_special_diet = models.CharField(max_length=255, default="NO", null=True, blank=True)
    special_diet = models.TextField(max_length=100, null=True, blank=True)
    if_use_caffein = models.CharField(max_length=255, default="NO", null=True, blank=True)
    caffein_daily_amt = models.CharField(max_length=255, null=True, blank=True)
    is_sadder = models.CharField(max_length=255, default="NO", null=True, blank=True)
    if_lost_interest = models.CharField(max_length=255, default="NO", null=True, blank=True)
    have_will = models.CharField(max_length=255, default="NO", null=True, blank=True)
    social_hist = models.TextField(max_length=400, null=True, blank=True)
    fam_hist = models.TextField(max_length=400, null=True, blank=True)


    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.patient_no

    def get_absolute_url(self):
        return reverse('registration_models_detail', args=(self.patient_no,))

    def get_update_url(self):
        return reverse('registration_models_update', args=(self.patient_no,))

    def create_patient_account(self):
        errors = {}

        try:
            CustomUser.object.get(email=self.email)
        except:
            errors['email'] = 'email exists'
        try:
            CustomUser.object.get(id_number=self.id_number)
        except:
            errors['id_number'] = 'The id number is not unique. A patient is registered with the same ip'
        if errors:
            return errors
        try:
            user = CustomUser.objects.create(email=self.email, is_patient=True, id_number=self.id_number, phone_number=self.phone,
                                             first_name=self.first_sname, last_name=self.last_name)
            user.save()
        except:
            errors['others'] = 'Something went wrong while creating an account patient. Contact the admin.'

        return errors



class Children(models.Model):

    patient_no = models.ForeignKey('Patient', on_delete=models.CASCADE,
                             verbose_name='patient_no',
                             related_name='children')
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255, default="NO", null=True, blank=True)
    age = models.CharField(max_length=255, default="NO", null=True, blank=True)


    class Meta:
        verbose_name = 'child'
        verbose_name_plural = 'children'
        ordering = ('last_updated',)

    def __str__(self):
        return self.pk


    def __unicode__(self):
        return u'%s' % self.pk


class Allergies(models.Model):
        allergy_name = models.CharField(max_length=200)

        class Meta:
            verbose_name = 'Allergy'
            verbose_name_plural = 'Allergies'

        def __str__(self):
            return self.pk

        def __unicode__(self):
            return u'%s' % self.pk


class County(models.Model):
        County = models.CharField(max_length=2550)


class MedicationHistory(models.Model):
        Disease = models.CharField(max_length=2550)


class InsuranceCompanies(models.Model):
    Name = models.CharField(max_length=2550)


class Medication(models.Model):

    patient_no = models.ForeignKey('Patient', on_delete=models.CASCADE,
                             verbose_name='patient_no',
                             related_name='medication')
    created = DateTimeField(auto_now_add=True, editable=False)
    last_updated = DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=255, default="NO", null=True, blank=True)
    age = models.CharField(max_length=255, default="NO", null=True, blank=True)

    class Meta:
        verbose_name = 'child'
        verbose_name_plural = 'children'
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.pk
