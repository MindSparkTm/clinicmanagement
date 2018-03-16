from django.contrib import admin
from django import forms
from .models import models

class modelsAdminForm(forms.ModelForm):

    class Meta:
        model = models
        fields = '__all__'


class modelsAdmin(admin.ModelAdmin):
    form = modelsAdminForm
    list_display = ['slug', 'created', 'last_updated', 'systolic', 'diastolic', 'temperature', 'oxygen_saturation', 'urinalysis', 'heart_rate', 'others', 'attending_nurse', 'patient_no', 'first_name', 'last_name', 'middle_name','triage_id', 'height', 'weight','random_glucose']

admin.site.register(models, modelsAdmin)


