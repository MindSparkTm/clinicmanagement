from django import forms
from .models import patientVisit


class patientVisitForm(forms.ModelForm):
    class Meta:
        model = patientVisit
        fields = ['name', 'patient_no', 'radiology_no', 'notes', 'diagnosis', 'prescription_id', 'status', 'triage_id']


