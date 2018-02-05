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

# labChoices =  {0: "Valentis Health", 1: " 124/80", 2: " 88", 3: "38.0", 4: "90.0", 7: "Medications", 8: "Alergies",
#      10: "Alergies",
#      13: " None", 14: " None", 15: " None", 16: " None", 18: " None", 19: " None", 22: "Haemoglobin estimation(Hb)", 28:
#          "Leucocyte diff count", 34: "Leucocyte Total count", 40: "Hb and diff count", 46: "Erythrocyte count",
#      52: "Packed Cell Volume", 58: "Full blood count", 64: "ESR", 75: "Prothrombin index(PI) / INR",
#      81: "PI / INR dosage information ", 92: "Blood group(A B O)", 98: "Groupting: Rh Antigen", 104: " Direct Coombs",
#      110: "Indirect Coombs", 116: "Syphilis Serology", 122: "Malaria: Antigen", 128: "Parasite in blood smear",
#      134: "Concentration techniques for parasite", 140: "TSH", 146:
#          "Potassium", 152: "sodium", 158: "Potassium / sodium / Chloride / Creatinine ", 164: "Creatinine", 170: "Urea",
#      176:"Urea & Electrolytes only", 182: "Uric acid", 188: "Glucose - random/fasting", 194: "HbA1C",
#      205: "Cholestrol - Total",
#      211: "Cholestral/HDL", 217: "Triglycerides", 223: "LDL Cholestrol", 229: "Amylase", 235: "Alkaline Phosphate", 241:
#          "Bilirubin: Total", 247: "Bilirubin: Conjugated",
#                253: "AST(SGOT)", 259: "ALT(SGPT)", 265: "LDH", 271: "Gamma GT", 282: "HIV viral load",
#                288: "CD 4/8 count", 294: "IHepatitis: AIGM antibody", 300: "Hepatitis: B surface antigen",
#                306: "C-reactive protein", 312: "Urine dipstick(per stick)", 318: "urine - microscopy",
#                324: "urine - micro/culture", 330: "Sputum - gram", 336: "Sputum - culture", 342: "Direct prep: AFB",
#                348: "LOcult blood", 354: "Faeces", 365: "Patient History", 371: "Total lg E",
#                377: "Inhalant Screen (phadiatop)", 383: "Rast per allergen", 389: "Iron", 395: "Ferritin",
#                401: "Soluble Transferrin receptor", 407: "CK-MB", 418: "Tropin T or I",
#                429: "Haemoglobin Estimation(Hb)", 435: "Blood grouping (ABO/RH Antigen) Creatine", 441: "Direct Coombs",
#                447: "Hepatitis B Surface antigen", 453: "Rubella lg G", 459: "Syphilis", 465: "HIV: Elisa", 471: "FSH",
#                482: "LH", 488: "Alkaline Phosphate", 494: "ALT(SGPT)", 500: "AST(SGOT)",
#                506: "Bilirubin: Total/Conjugated", 512: "LDH", 518: "Gamma GT"
#                }


class Labs(models.Model):
    # Fields
    slug = extension_fields.AutoSlugField(populate_from='lab_name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    lab_name = models.TextField(max_length=100, null=True, blank=True)
    h01 = models.BooleanField(default=False)
    h02 = models.BooleanField(default=False)
    h03 = models.BooleanField(default=False)
    h04 = models.BooleanField(default=False)
    h05 = models.BooleanField(default=False)
    h06 = models.BooleanField(default=False)
    h07 = models.BooleanField(default=False)
    h08 = models.BooleanField(default=False)
    h09 = models.BooleanField(default=False)
    c01 = models.BooleanField(default=False)
    c02 = models.BooleanField(default=False)
    p01 = models.BooleanField(default=False)
    p02 = models.BooleanField(max_length=100, default=False)
    p03 = models.BooleanField(default=False)
    p04 = models.BooleanField(default=False)
    p05 = models.BooleanField(default=False)
    p06 = models.BooleanField(default=False)
    mbs01 = models.BooleanField(default=False)
    mbs02 = models.BooleanField(default=False)
    mbs03 = models.BooleanField(default=False)
    ge01 = models.BooleanField(default=False)
    lks01 = models.BooleanField(default=False)
    lks02 = models.BooleanField(default=False)
    lks03 = models.BooleanField(default=False)
    lks04 = models.BooleanField(default=False)
    lks05 = models.BooleanField(default=False)
    lks06 = models.BooleanField(default=False)
    lks07 = models.BooleanField(default=False)
    gm01 = models.BooleanField(default=False)
    gm02 = models.BooleanField(default=False)
    gm03 = models.BooleanField(default=False)
    lm01 = models.BooleanField(default=False)
    lm02 = models.BooleanField(default=False)
    lm03 = models.BooleanField(default=False)
    lm04 = models.BooleanField(default=False)
    lpg01 = models.BooleanField(default=False)
    lpg02 = models.BooleanField(default=False)
    lpg03 = models.BooleanField(max_length=100, default=False)
    lpg04 = models.BooleanField(default=False)
    lpg05 = models.BooleanField(default=False)
    lpg06 = models.BooleanField(default=False)
    lpg06 = models.BooleanField(default=False)
    lpg07 = models.BooleanField(default=False)
    lpg08 = models.BooleanField(default=False)
    hv01 = models.BooleanField(default=False)
    hv02 = models.BooleanField(default=False)
    hv03 = models.BooleanField(default=False)
    i01 = models.BooleanField(default=False)
    i02 = models.BooleanField(default=False)
    i03 = models.BooleanField(default=False)
    m01 = models.BooleanField(default=False)
    m02 = models.BooleanField(default=False)
    m03 = models.BooleanField(default=False)
    M04 = models.BooleanField(default=False)
    m05 = models.BooleanField(default=False)
    m06 = models.BooleanField(default=False)
    m07 = models.BooleanField(default=False)
    m08 = models.BooleanField(default=False)
    g01 = models.BooleanField(max_length=200, default=False)
    other = models.TextField(max_length=100, null=True, blank=True)
    diagnosis = models.TextField(max_length=100, null=True, blank=True)
    h01_alergy = models.BooleanField(default=False)
    h02_alergy = models.BooleanField(default=False)
    h03_alergy = models.BooleanField(default=False)
    h04_alergy = models.BooleanField(default=False)
    h06_alergy = models.BooleanField(default=False)
    h07_alergy = models.BooleanField(default=False)
    h08_alergy = models.BooleanField(max_length=100, default=False)
    c01_iron_studies = models.BooleanField(default=False)
    c01_cardiac_markers = models.BooleanField(max_length=100, default=False)
    c02_cardiac_markers = models.BooleanField(max_length=100, default=False)
    c02_cardiac_markers_1 = models.BooleanField(max_length=100, default=False)
    lks01_antenatal_screen = models.BooleanField(default=False)
    lks02_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks04_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks05_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks06_antenatal_screen = models.BooleanField(max_length=100, default=False)
    lks07_antenatal_screen = models.BooleanField(max_length=100, default=False)
    gm01_antenatal_screen = models.BooleanField(default=False)
    fsh_menopausal_screen = models.BooleanField(default=False)
    oestradiol_menopausal_screen = models.BooleanField(max_length=100, default=False)
    albumin_menopausal_screen = models.BooleanField(default=False)
    hv02_menopausal_screen = models.BooleanField(max_length=100, default=False)
    hv03_menopausal_screen = models.BooleanField(default=False)
    ast_menopausal_screen = models.BooleanField(max_length=100, default=False)
    i01_menopausal_screen = models.BooleanField(max_length=100, default=False)
    i02_menopausal_screen = models.BooleanField(default=False)
    i03_menopausal_screen = models.TextField(max_length=100, null=True, blank=True)
    patient_no = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('labs_labs_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('labs_labs_update', args=(self.slug,))


class Radiology(models.Model):
    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    lpm_date = models.BooleanField(default=False)
    could_b_pregrant = models.TextField(max_length=100, null=True, blank=True)
    examination = models.TextField(max_length=200, null=True, blank=True)
    clinical_indication = models.TextField(max_length=200, null=True, blank=True)
    intra_orbital_fb_hist = models.BooleanField(default=False)
    intracranial_clip = models.BooleanField(default=False)
    pacemaker = models.BooleanField(default=False)
    cochlear_implants = models.BooleanField(default=False)
    prosthetic_hrt_valve = models.BooleanField(default=False)
    pregnancy = models.BooleanField(default=False)
    recent_surgery = models.BooleanField(default=False)
    patient_info = models.BooleanField(default=False)
    diabetic_metformin = models.BooleanField(default=False)
    allergic_contrast = models.BooleanField(default=False)
    other_allergies = models.BooleanField(max_length=100, default=False)
    kidney_problems = models.BooleanField(default=False)
    anticoagulant_drugs = models.BooleanField(default=False)
    egfr_result = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    patient_no = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('labs_radiology_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('labs_radiology_update', args=(self.slug,))


class RadiologyResult(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    patient_no = models.CharField(max_length=30)
    results = models.TextField(max_length=400)
    tests_done = models.TextField(max_length=400)


    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('radiologyresult_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('radiologyresult_update', args=(self.slug,))


class LabResults(models.Model):

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='patient_no', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    patient_no = models.TextField(max_length=100)
    tests_done = models.TextField(max_length=400)
    test_results = models.TextField(max_length=400)


    class Meta:
        ordering = ('last_updated',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('labresults_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('labresults_update', args=(self.slug,))
