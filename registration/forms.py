from django import forms
from .models import Patient, Child
from django.forms import Textarea
from django.forms.formsets import BaseFormSet


class PatientForm(forms.ModelForm):
    IDCHOICES = (
        ('ID', 'ID Number'),
        ('Passport', 'Passport Number'),
    )
    id_type = forms.CharField(widget=forms.Select(choices=IDCHOICES, attrs={
        'class': 'select-box',
    }))

    YESNO = (
        ('Yes', 'Yes'),
        ('No','No')
    )

    if_smoker = forms.CharField(widget=forms.Select(choices=YESNO, attrs={
        'class': 'select-box',
    }))

    GENDERCHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = forms.CharField(widget=forms.Select(choices=GENDERCHOICES,
                                                 attrs={
                                                     'class': 'select-box',
                                                 }
                                                 ))
    dob = forms.CharField(widget=forms.TextInput(attrs={
                                                     'class': 'mdl-textfield__input',
        'type':'date'
                                                 }
                                                 ))

    class Meta:
        model = Patient

        exclude = ('patient_no', 'created')


class MedicationForm(forms.Form):
    medication = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Medication',
        }),
        required=False)
    dosage = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Dosage',
        }))

    route = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Route',
        }))

    frequency = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'frequency',
        }))

    patient_no = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Patient ID',
        }))


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['child_name', 'child_age', 'child_dob']


class MedicationFormSet(BaseFormSet):
    def clean(self):

        if any(self.errors):
            return

        for form in self.forms:
            if form.cleaned_data:
                dosage = form.cleaned_data['dosage']
                medication = form.cleaned_data['medication']
                route = form.cleaned_data['route']
                frequency = form.cleaned_data['frequency']

                # Check that all links have both an anchor and URL
                if (dosage and not medication) or (route and not medication) or (frequency and not medication):
                    raise forms.ValidationError(
                        'You must enter a medication.',
                        code='missing_medication'
                    )
