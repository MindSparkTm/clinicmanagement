from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import patientVisit
from .forms import patientVisitForm
from registration.models import models as Patient


class patientVisitListView(ListView):
    model = patientVisit


class patientVisitCreateView(CreateView):
    model = patientVisit
    form_class = patientVisitForm

    def get_context_data(self, **kwargs):
        context = super(patientVisitCreateView, self).get_context_data(**kwargs)

        context['doc_waiting_list'] = Patient.objects.filter(status="3")
        return context


class patientVisitDetailView(DetailView):
    model = patientVisit


class patientVisitUpdateView(UpdateView):
    model = patientVisit
    form_class = patientVisitForm

