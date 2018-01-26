from django.contrib import admin
from django import forms
from .models import models

class modelsAdminForm(forms.ModelForm):

    class Meta:
        model = models
        fields = '__all__'


class modelsAdmin(admin.ModelAdmin):
    form = modelsAdminForm
    list_display = ['slug', 'created', 'last_updated', 'systolic', 'diastolic', 'temperature', 'oxygen_saturation', 'urinalysis', 'heart_rate', 'others', 'attending_nurse', 'patient_id', 'first_name', 'last_name', 'middle_name']
    readonly_fields = ['slug', 'created', 'last_updated', 'systolic', 'diastolic', 'temperature', 'oxygen_saturation', 'urinalysis', 'heart_rate', 'others', 'attending_nurse', 'patient_id', 'first_name', 'last_name', 'middle_name']

admin.site.register(models, modelsAdmin)


