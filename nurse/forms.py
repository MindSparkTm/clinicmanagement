from django import forms
from .models import Nurse


class ModelsForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ['systolic', 'diastolic', 'temperature', 'oxygen_saturation', 'urinalysis', 'heart_rate', 'others', 'attending_nurse', 'patient_no', 'first_name', 'last_name', 'middle_name', 'height', 'weight', 'random_glucose']


