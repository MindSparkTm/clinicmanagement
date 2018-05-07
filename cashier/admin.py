from django.contrib import admin
from django import forms
from .models import PatientBill


# Register your models here.


class PatientBilladmin(admin.ModelAdmin):
    list_display = ['created','patientid', 'totalbill','billbreakdown','invoiceid']
admin.site.register(PatientBill, PatientBilladmin)
