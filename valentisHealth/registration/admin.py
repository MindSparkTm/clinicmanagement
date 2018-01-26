from django.contrib import admin
from django import forms
from .models import models

class modelsAdminForm(forms.ModelForm):

    class Meta:
        model = models
        fields = '__all__'


class modelsAdmin(admin.ModelAdmin):
    form = modelsAdminForm
    list_display = ['patient_id', 'created', 'last_updated', 'first_name', 'middle_name', 'last_name', 'Gender', 'street_name', 'apartment_name', 'postal_code', 'postal_address', 'city', 'country', 'age', 'next_of_kin', 'n_of_kin_rel', 'email', 'phone', 'primary_insurance', 'secondary_insurance', 'pri_ins_sub', 'sec_ins_sub', 'other_ins_subscriber', 'subscriber_relationship', 'sub_address', 'ss_number', 'sub_ss_number', 'alt_phone', 'sub_work_phone', 'dob', 'sub_dob', 'sub_employer']
    readonly_fields = ['patient_id', 'created', 'last_updated', 'first_name', 'middle_name', 'last_name', 'Gender', 'street_name', 'apartment_name', 'postal_code', 'postal_address', 'city', 'country', 'age', 'next_of_kin', 'n_of_kin_rel', 'email', 'phone', 'primary_insurance', 'secondary_insurance', 'pri_ins_sub', 'sec_ins_sub', 'other_ins_subscriber', 'subscriber_relationship', 'sub_address', 'ss_number', 'sub_ss_number', 'alt_phone', 'sub_work_phone', 'dob', 'sub_dob', 'sub_employer']

admin.site.register(models, modelsAdmin)


