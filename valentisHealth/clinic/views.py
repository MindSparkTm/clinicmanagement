from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import patientVisit
from .forms import patientVisitForm
from registration.models import models as Patient
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from nurse.models import models as Triage

class patientVisitListView(ListView):
    model = patientVisit

    def get_context_data(self, **kwargs):
        context = super(patientVisitListView, self).get_context_data(**kwargs)

        try:
            context['all_patients'] = Patient.objects.all()

        except:
            raise Http404('Requested user not found.')

        return context


class patientVisitCreateView(CreateView):
    model = patientVisit
    form_class = patientVisitForm

    def get_context_data(self, **kwargs):
        context = super(patientVisitCreateView, self).get_context_data(**kwargs)

        try:
            context['waiting_list'] = Patient.objects.filter(status="3")
            context['show_waiting_list'] = True
            context['link'] = 'clinic/patientvisit/doctor'
        except:
            raise Http404('Requested user not found.')

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
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])
            #status 0 means patient's session ended
            patient_object.status = 0
            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")

    def get_context_data(self, **kwargs):
        print(self.kwargs['patient_no'], "is user")

        context = super(DoctorVisit, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])

            context['waiting_list'] = Patient.objects.filter(status="3")
            #-4 out of labs, -5 out of radiology
            context['from_labs'] = Patient.objects.filter(status="-4")
            context['from_radiology'] = Patient.objects.filter(status="-5")
            context['patient'] = patient_object
            context['triage'] = Triage.objects.get(patient_no=self.kwargs['patient_no'])
        except:
            raise Http404('Requested user not found.')


        return context


