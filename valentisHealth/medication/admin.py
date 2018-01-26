from django.contrib import admin
from django import forms
from .models import models

class modelsAdminForm(forms.ModelForm):

    class Meta:
        model = models
        fields = '__all__'


class modelsAdmin(admin.ModelAdmin):
    form = modelsAdminForm
    list_display = ['slug', 'created', 'last_updated', 'prescription_id', 'patients_id', 'patient_name', 'address', 'phone_number', 'signature', 'prescription']
    readonly_fields = ['slug', 'created', 'last_updated', 'prescription_id', 'patients_id', 'patient_name', 'address', 'phone_number', 'signature', 'prescription']

admin.site.register(models, modelsAdmin)


