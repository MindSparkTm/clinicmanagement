from django import forms
from .models import patientVisit


class patientVisitForm(forms.ModelForm):
    class Meta:
        model = patientVisit
        fields = ['name', 'patient_no', 'radiology_no', 'notes', 'diagnosis', 'status', 'examination', 'plan_of_managemnt', 'query_diagnosis', 'his_presenting_illness']

