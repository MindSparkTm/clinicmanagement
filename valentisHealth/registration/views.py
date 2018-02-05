from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import models, Children, Medication
from .forms import modelsForm, MedicationForm, ChildrenForm, MedicationFormSet
from django.http import HttpResponseRedirect

class modelsListView(ListView):
    model = models


class modelsCreateView(CreateView):
    model = models
    form_class = modelsForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status = 2
        instance.save()
        print(instance.status)

        return HttpResponseRedirect("/registration/models/create/?sucess=true")


class modelsDetailView(DetailView):
    model = models


class SearchPatientView(CreateView):
    model = models
    form_class = modelsForm

    def get_template_names(self):
        return 'registration/search_patient.html'


class CreateMedication(CreateView):
    medications = Medication
    form_class = MedicationForm

    medication_formset = MedicationFormSet

