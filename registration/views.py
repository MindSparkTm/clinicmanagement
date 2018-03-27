from django.views.generic import ListView, UpdateView, CreateView, View, DetailView
from .models import Patient, Child
from .forms import PatientForm
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, reverse
from django.shortcuts import render
from django.forms import inlineformset_factory
# from django.contrib.auth.mixins import UserPassesTestMixin
# from valentisHealth.authenticator import *

class LandingView(ListView):
    model = Patient

    def get_template_names(self):
        return 'registration/search_patient.html'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm

    def get_context_data(self, **kwargs):
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        context['new'] = True

        return context

    def get_template_names(self):
        print("+++____+++___+++", self.request.POST.dict())
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

        return render(self.request, 'registration/patient_form.html', {'success': message, 'new':True})
        # return HttpResponseRedirect("/registration/models/create/?sucess=true")


class PatientDetailView(DetailView):
    def get_object(self, queryset=None, **kwargs):
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])

        return patient_object

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


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'registration/patient_form.html'

    def get_object(self, **kwargs):
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])

        return patient_object

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()

        context = self.get_context_data()
        child_form = context['child_formset']
        if child_form.is_valid():
            self.object = form.save()
            child_form.instance = self.object
            child_form.save()

        return render(self.request, self.template_name, {'form': form, 'success':"Updated the patient's history successfully", 'child_formset':child_form})

    def get_context_data(self, **kwargs):
        context = super(PatientUpdateView, self).get_context_data(**kwargs)
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        context['patient'] = patient_object

        ChildFormSet = inlineformset_factory(Patient, Child, exclude=())
        if self.request.POST:
            context['child_formset'] = ChildFormSet(self.request.POST)
        else:
            context['child_formset'] = ChildFormSet()

        return context
