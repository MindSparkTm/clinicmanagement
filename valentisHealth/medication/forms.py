from django import forms
from .models import models


class modelsForm(forms.ModelForm):
    class Meta:
        model = models
        fields = ['patient_no', 'patient_name', 'address','email', 'phone_number', 'prescription','triage_id']
