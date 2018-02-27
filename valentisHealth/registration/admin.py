from django.contrib import admin
from django import forms
from .models import Patient, Allergies, County


class modelsAdminForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class modelsAdmin(admin.ModelAdmin):
    form = modelsAdminForm

list_display = ['patient_no', 'created', 'last_updated', 'status', 'first_name', 'middle_name', 'last_name', 'gender',
                'street_name', 'apartment_name', 'postal_code', 'postal_address', 'city', 'country',
                'next_of_kin', 'n_of_kin_rel', 'email', 'phone', 'primary_insurance', 'secondary_insurance',
                'pri_ins_sub', 'sec_ins_sub', 'other_ins_subscriber', 'subscriber_relationship', 'sub_address',
                'ss_number', 'sub_ss_number', 'alt_phone', 'sub_work_phone', 'dob', 'sub_dob', 'sub_employer',
                'age', 'occupation', 'marital_status', 'spouse', 'no_children', 'childrens', 'prev_docs',
                'medical_information', 'alergies', 'preferred_pharmacy', 'last_phys_examination', 'last_blood_work',
                'last_colonoscopy', 'last_tetanus_shot', 'last_menstrual', 'last_pap_smear', 'last_mammogram',
                'dexa', 'no_pregnancies', 'miscourages', 'living_children', 'methods_of_contraception', 'surgeries',
                'genetic_diseases', 'if_smoker', 'cigar_per_day', 'no_of_yr_smoking', 'if_chew_tobacco',
                'yrs_chewing_tobacco', 'if_quit_before', 'tobacco_quit_duration', 'if_drink_alcohol',
                'alocohol_type', 'alcohol_frequency', 'if_drug_used', 'drug_type', 'when_drug_used', 'if_exercise',
                'exercise_freq', 'if_special_diet', 'special_diet', 'if_use_caffein', 'caffein_daily_amt',
                'is_sadder', 'if_lost_interest', 'have_will', 'session_id',
                'social_hist', 'fam_hist']

admin.site.register(Patient, modelsAdmin)

