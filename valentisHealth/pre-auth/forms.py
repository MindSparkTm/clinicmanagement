from django import forms
from .models import pre_auth


class pre_authForm(forms.ModelForm):
    class Meta:
        model = pre_auth
        fields = ['name', 'reference_no', 'authority_type', 'provider', 'ward', 'date_admitted', 'date_provided', 'notes', 'claim', 'limit', 'batch_no', 'date_reported', 'admit_days', 'anniv', 'daily_bed_limit', 'type', 'authorised_by']


