from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import patientVisit
from .forms import patientVisitForm
from registration.models import models as Patient
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from nurse.models import models as Triage

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

class DoctorVisit(CreateView):
    model = patientVisit
    form_class = patientVisitForm

    def get_template_names(self):
        return 'clinic/visitform_copy.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_id=form.cleaned_data['patient_id'])
            patient_object.status = 4
            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")

    def get_context_data(self, **kwargs):
        print(self.kwargs['patient_id'], "is user")

        context = super(DoctorVisit, self).get_context_data(**kwargs)

        try:
            print(id, "user")
            patient_object = Patient.objects.get(patient_id=self.kwargs['patient_id'])

            context['doc_waiting_list'] = Patient.objects.filter(status="3")
            context['patient'] = patient_object
            context['triage'] = Triage.objects.get(patient_id=self.kwargs['patient_id'])
            # patient_object.status = 3
        except:
            raise Http404('Requested user not found.')


        return context


