from django import forms
from .models import models
from django.forms import Textarea

class modelsForm(forms.ModelForm):
    class Meta:
        model = models
        fields = ['patient_id', 'first_name', 'middle_name', 'last_name', 'Gender', 'street_name', 'apartment_name', 'postal_code', 'postal_address', 'city', 'country', 'age', 'next_of_kin', 'n_of_kin_rel', 'email', 'phone', 'primary_insurance', 'secondary_insurance', 'pri_ins_sub', 'sec_ins_sub', 'other_ins_subscriber', 'subscriber_relationship', 'sub_address', 'ss_number', 'sub_ss_number', 'alt_phone', 'sub_work_phone', 'dob', 'sub_dob', 'sub_employer']
        widgets = {
            'patient_id': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
