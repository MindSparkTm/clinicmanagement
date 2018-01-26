from django.contrib import admin
from django import forms
from .models import pre_auth

class pre_authAdminForm(forms.ModelForm):

    class Meta:
        model = pre_auth
        fields = '__all__'


class pre_authAdmin(admin.ModelAdmin):
    form = pre_authAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'reference_no', 'authority_type', 'provider', 'ward', 'date_admitted', 'date_provided', 'notes', 'claim', 'limit', 'batch_no', 'date_reported', 'admit_days', 'anniv', 'daily_bed_limit', 'type', 'authorised_by']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'reference_no', 'authority_type', 'provider', 'ward', 'date_admitted', 'date_provided', 'notes', 'claim', 'limit', 'batch_no', 'date_reported', 'admit_days', 'anniv', 'daily_bed_limit', 'type', 'authorised_by']

admin.site.register(pre_auth, pre_authAdmin)


