from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import models, Children, Medication, Uploads
from .forms import modelsForm, MedicationForm, ChildrenForm, MedicationFormSet
from django.http import HttpResponseRedirect
from .models import Patient
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, reverse
# from django.contrib.auth.mixins import UserPassesTestMixin
# from valentisHealth.authenticator import *

class modelsListView(ListView):
    model = Patient

    # def test_func(self):
    #     return is_callcenter(self.request)

    def get_template_names(self):
        return 'registration/search_patient.html'

class modelsCreateView(CreateView):
    model = Patient
    form_class = modelsForm

    def get_template_names(self):
        return 'registration/models_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status = 2

        instance.save()

        return HttpResponseRedirect("/registration/models/create/?sucess=true")


class modelsDetailView(ListView):
    model = Patient

    def get_template_names(self):
        return 'registration/history_form.html'

    # def get_object(self):
    #     return get_object_or_404(models, pk=request.session['user_id'])

    def get_context_data(self, **kwargs):

        context = super(modelsDetailView, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            context['patient'] = patient_object

        except:
            raise Http404('Requested user not found.')

        return context

class SearchPatientView(CreateView):
    model = Patient
    form_class = modelsForm

    def get_template_names(self):
        return 'medication/models_search.html'




class CreateMedication(CreateView):
    medications = Medication
    form_class = MedicationForm

    medication_formset = MedicationFormSet



def patientUpdateView(request, patient_no):
    try:
        patient_object = Patient.objects.get(patient_no=patient_no)
        patient_object.status = 2
        patient_object.save()

    except:
        raise Http404('Requested user not found.')
    return HttpResponseRedirect("/registration/", {})

# class patientUpdateView_(ListView):
#     model = models
#     form_class = modelsForm
#
#     def get_context_data(self, **kwargs):
#
#         context = super(patientUpdateView, self).get_context_data(**kwargs)
#
#         try:
#             patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
#             patient_object.status = 2
#             patient_object.save()
#
#         except:
#             raise Http404('Requested user not found.')
#
#         return HttpResponseRedirect("/registration/models/create/?sucess=true")