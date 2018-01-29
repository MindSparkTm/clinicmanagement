from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import patientVisit
from .forms import patientVisitForm


class patientVisitListView(ListView):
    model = patientVisit


class patientVisitCreateView(CreateView):
    model = patientVisit
    form_class = patientVisitForm


class patientVisitDetailView(DetailView):
    model = patientVisit


class patientVisitUpdateView(UpdateView):
    model = patientVisit
    form_class = patientVisitForm

