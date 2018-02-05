from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import models
from .forms import modelsForm
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect, reverse
from registration.models import models as Patient
from clinic.models import Diagnosis

class modelsListView(ListView):
    model = models


class modelsCreateView(CreateView):
    model = models
    form_class = modelsForm


    def form_valid(self, form):
        instance = form.save(commit=False)
        # status 4 means patient's in lab
        instance.status = 0
        instance.save()

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

