from django import forms
from .models import Patient
from django.forms import Textarea
from django.forms.formsets import BaseFormSet

class modelsForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['patient_no', 'first_name', 'middle_name', 'last_name', 'gender',
                  'street_name', 'apartment_name', 'postal_code', 'postal_address',
                  'city', 'country', 'age', 'next_of_kin', 'n_of_kin_rel', 'email',
                  'phone', 'primary_insurance', 'secondary_insurance', 'pri_ins_sub',
                  'sec_ins_sub', 'other_ins_subscriber', 'subscriber_relationship',
                  'sub_address', 'ss_number', 'sub_ss_number', 'alt_phone', 'sub_work_phone',
                  'dob', 'sub_dob', 'sub_employer', 'if_smoker', 'if_chew_tobacco',
                  'if_drink_alcohol', 'if_drug_used', 'if_exercise', 'if_special_diet',
                  'if_use_caffein', 'is_sadder', 'have_will', 'if_quit_before', 'uploaded_file'
                  'social_hist','fam_hist'
                  ]

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




class ChildrenForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChildrenForm, self).__init__(*args, **kwargs)

        self.fields['patient_no'] = forms.CharField(
            max_length=30,
            initial=self.user.first_name,
            widget=forms.TextInput(attrs={
                'placeholder': 'Patient ID',
            }))

        self.fields['name'] = forms.CharField(
                                        max_length=30,
                                        initial = self.user.first_name,
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Name',
                                        }))
        self.fields['Age'] = forms.CharField(
                                        max_length=30,
                                        initial = self.user.last_name,
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Age',
                                        }))


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


