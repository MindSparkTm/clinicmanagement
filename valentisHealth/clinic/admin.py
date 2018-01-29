from django.contrib import admin
from django import forms
from .models import patientVisit

class patientVisitAdminForm(forms.ModelForm):

    class Meta:
        model = patientVisit
        fields = '__all__'


class patientVisitAdmin(admin.ModelAdmin):
    form = patientVisitAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'patient_id', 'visit_id', 'radiology_no', 'notes', 'diagnosis', 'prescription_id', 'status']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'patient_id', 'visit_id', 'radiology_no', 'notes', 'diagnosis', 'prescription_id', 'status']

admin.site.register(patientVisit, patientVisitAdmin)


