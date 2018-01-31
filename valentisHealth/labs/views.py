from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import labs, radiology
from .forms import labsForm, radiologyForm
from django.http import HttpResponseRedirect

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

        return HttpResponseRedirect("")

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

