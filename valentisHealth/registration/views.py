from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Patient, Child, Medication, Uploads
from .forms import PatientForm, MedicationForm, ChildForm, MedicationFormSet, ChildFormSet
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, reverse
from django.shortcuts import render
from django.forms.formsets import formset_factory
from django.db import transaction

# from django.contrib.auth.mixins import UserPassesTestMixin
# from valentisHealth.authenticator import *

class PatientListView(ListView):
    model = Patient

    # def test_func(self):
    #     return is_callcenter(self.request)

    def get_template_names(self):
        return 'registration/search_patient.html'


class ChildCreate(CreateView):
    model = Child
    fields = ['child_name', 'child_age']
    success_url = ""

    def get_context_data(self, **kwargs):
        data = super(ChildCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['children'] = ChildFormSet(self.request.POST)
        else:
            data['children'] = ChildFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        children = context['children ']
        with transaction.atomic():
            self.object = form.save()

            if children .is_valid():
                children.instance = self.object
                children.save()
        return super(ChildCreate, self).form_valid(form)


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm

    def get_template_names(self):
        return 'registration/patient_form.html'


    def form_valid(self, form):

        instance = form.save(commit=False)
        instance.status = 2
        errors_check = instance.create_patient_account(self.request)
        print('error detected are', errors_check)
        if errors_check:
            print('error occurred', errors_check)
            return render(self.request, 'registration/patient_form.html', {'errors': errors_check, 'form':form})
        instance.save()

        message = "Successfully created patient and patient account. Login detail for the mobile app are sent to their email"

        return render(self.request, 'registration/patient_form.html', {'success': message})
        # return HttpResponseRedirect("/registration/models/create/?sucess=true")


class PatientDetailView(ListView):
    model = Patient

    def get_template_names(self):
        return 'registration/history_form.html'

    # def get_object(self):
    #     return get_object_or_404(models, pk=request.session['user_id'])

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            context['patient'] = patient_object

        except:
            raise Http404('Requested user not found.')

        return context


class SearchPatientView(CreateView):
    model = Patient
    form_class = PatientForm

    def get_template_names(self):
        return 'medication/models_search.html'


class CreateMedication(CreateView):
    medications = Medication
    form_class = MedicationForm

    medication_formset = MedicationFormSet


def PatientUpdateView(request, patient_no):
    try:
        patient_object = Patient.objects.get(patient_no=patient_no)
        patient_object.status = 2
        patient_object.save()

    except:
        raise Http404('Requested user not found.')
    return HttpResponseRedirect("/registration/", {})
