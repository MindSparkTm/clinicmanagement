from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import labs, radiology
from .forms import labsForm, radiologyForm
from django.http import HttpResponseRedirect
from registration.models import models as Patient

class labsListView(ListView):
    model = labs


class labsCreateView(CreateView):
    model = labs
    form_class = labsForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status = 2
        instance.save()
        print(instance.status)


        doc_waiting_list = Patient.objects.filter(status="3")
        id = form.cleaned_data['patient_id']
        selected = Patient.objects.filter(patient_id=id)

        return HttpResponseRedirect("/clinic/patientvisit/create/", {doc_waiting_list, selected})

class labsDetailView(DetailView):
    model = labs


class labsUpdateView(UpdateView):
    model = labs
    form_class = labsForm


class radiologyListView(ListView):
    model = radiology


class radiologyCreateView(CreateView):
    model = radiology
    form_class = radiologyForm


class radiologyDetailView(DetailView):
    model = radiology


class radiologyUpdateView(UpdateView):
    model = radiology
    form_class = radiologyForm

