from django import forms
from .models import PatientBill


class PatientBillform(forms.ModelForm):
    patientid = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 'class': "mdl-textfield__input",
            }))
    totalbill = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "mdl-textfield__input"
            }))





    class Meta:
        model = PatientBill
        fields = ['patientid', 'totalbill']