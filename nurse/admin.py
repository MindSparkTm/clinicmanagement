from django.contrib import admin
from django import forms
from .models import Nurse

class ModelsAdminForm(forms.ModelForm):

    class Meta:
        model = Nurse
        fields = '__all__'


class ModelsAdmin(admin.ModelAdmin):
    form = ModelsAdminForm
    list_display = ['slug', 'created', 'last_updated', 'systolic', 'diastolic', 'temperature', 'oxygen_saturation', 'urinalysis', 'heart_rate', 'others', 'attending_nurse', 'patient_no', 'first_name', 'last_name', 'middle_name','triage_id', 'height', 'weight','random_glucose']

admin.site.register(Nurse, ModelsAdmin)


