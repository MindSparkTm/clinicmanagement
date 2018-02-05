from django.contrib import admin
from django import forms
from .models import patientVisit, Diagnosis

class patientVisitAdminForm(forms.ModelForm):

    class Meta:
        model = patientVisit
        fields = '__all__'


class patientVisitAdmin(admin.ModelAdmin):
    form = patientVisitAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'patient_no', 'visit_id', 'radiology_no', 'notes', 'diagnosis', 'prescription_id', 'status']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'patient_no', 'visit_id', 'radiology_no', 'notes', 'diagnosis', 'prescription_id', 'status']

admin.site.register(patientVisit, patientVisitAdmin)


class DiagnosisAdminForm(forms.ModelForm):

    class Meta:
        model = Diagnosis
        fields = '__all__'


class DiagnosisAdmin(admin.ModelAdmin):
    form = DiagnosisAdminForm
    list_display = ['created', 'last_updated', 'code', 'name']
    readonly_fields = ['created', 'last_updated', 'code', 'name']

admin.site.register(Diagnosis, DiagnosisAdmin)


