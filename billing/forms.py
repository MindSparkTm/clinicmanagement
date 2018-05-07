from django import forms
from .models import Billing


class Billingform(forms.ModelForm):
    service = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 'class': "mdl-textfield__input",
                 'placeholder': 'Enter Service Name',
                 'required': "True",

            }))
    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "mdl-textfield__input",
                'placeholder': 'Enter price',
                'required': "True",

            }))





    class Meta:
        model = Billing
        fields = ['service', 'price']