from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from registration.models import models as Patient

from valentisHealth.authenticator import *
from .forms import modelsForm
from .models import models

class modelsListView(ListView):
    model = models


class modelsCreateView(CreateView):
    model = models
    form_class = modelsForm

    def dispatch(self, request, *args, **kwargs):
        if is_nurse(self) or is_doctor(self) or is_callcenter(self):
            return super().dispatch(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/account/log-in/')

    def form_valid(self, form):
        instance = form.save(commit=False)
        # status 4 means patient's in lab
        instance.status = 0
        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            instance.triage_id = patient_object.session_id
        except:
            pass
        instance.save()

        # try:
        #     visit = patientVisit.objects.get(patient_no=self.kwargs['patient_no']).latest('created')
        #     prescr = models.objects.get(triage_id=self.kwargs['patient_no']).latest('created')
        #     visit.prescription_id = prescr.presscription_id
        # except:
        #     pass

        return HttpResponseRedirect("/medication/search")

    def get_context_data(self, **kwargs):
        context = super(modelsCreateView, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            patient_object.patient_name = patient_object.first_name + " " + patient_object.last_name
            context['patient'] = patient_object

        except:
            raise Http404('Requested user not found.')

        return context


class modelsDetailView(DetailView):
    model = models




class modelsUpdateView(UpdateView):
    model = models
    form_class = modelsForm


class ModelSearchView(View):
    model = models

    # def get_template_names(self):
    #     return 'medication/models_search.html'

    def get(self, request):

        return render(request, 'medication/models_search.html')

