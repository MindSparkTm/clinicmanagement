from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import labs, radiology
from .forms import labsForm, radiologyForm


class labsListView(ListView):
    model = labs


class labsCreateView(CreateView):
    model = labs
    form_class = labsForm


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

