from django.contrib import admin
from django import forms
from .models import Billing


# Register your models here.


class Billinginfo(admin.ModelAdmin):

    list_display = ['created', 'service', 'price']
admin.site.register(Billing, Billinginfo)
