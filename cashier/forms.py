from django import forms
from .models import PatientBill


class PatientBillform(forms.ModelForm):
    patientid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':"mdl-textfield__input",
                'id': "patientid",
                'placeholder':"Enter patient id",
                'required': "True",
            }))
    totalbill = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "mdl-textfield__input",
                'id': "totalbill",
                'placeholder': "TotalBill",
                'readonly': 'readonly',

            }))

    billbreakdown = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':"mdl-textfield__input bordered",
               'id': "billbreakdown",
                'width':"100%",
                'cols' : "12",
                'rows': "4",
                'readonly': 'readonly'

            }))

    invoiceid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "mdl-textfield__input",
                'id': "invoiceid",

    }))

    class Meta:
        model = PatientBill
        fields = ['patientid', 'totalbill','billbreakdown','invoiceid']