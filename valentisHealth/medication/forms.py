from django import forms
from .models import models


class modelsForm(forms.ModelForm):
    class Meta:
        model = models
        fields = ['prescription_id', 'patients_id', 'patient_name', 'address', 'phone_number', 'prescription']


