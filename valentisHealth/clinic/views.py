from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import patientVisit, Diagnosis
from .forms import patientVisitForm
from registration.models import models as Patient
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from nurse.models import models as Triage
from django.db.models import Q

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
            context['from_labs'] = Patient.objects.filter(Q(status="-4") | Q(status="-45"))
            context['from_radiology'] = Patient.objects.filter(Q(status="-5") | Q(status="-54"))
            context['link'] = 'clinic/patientvisit/doctor'
            context['clinic'] = True
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
            instance.triage_id = Triage.objects.filter(patient_no=self.kwargs['patient_no'])[0].triage_id
            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")

    def get_context_data(self, **kwargs):

        context = super(DoctorVisit, self).get_context_data(**kwargs)
        try:
            context['triage'] = Triage.objects.filter(patient_no=self.kwargs['patient_no'])[0]
        except:
            context['triage'] = Triage.objects.filter(patient_no=self.kwargs['patient_no'])

        try:

            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            print(patient_object.alergies)


            if patient_object.alergies is not None:

                #we will use ,,, tripple comma to seperate each alergy
                allergy_list = patient_object.alergies.split(",,,")

                #we will use :: to determine/seperate the alergy name and alergy reaction (dictionary - key value pair)
                allergies = [_.split("::") for _ in allergy_list]
                patient_object.alergies = allergies

            context['waiting_list'] = Patient.objects.filter(status="3")

            #-4 out of labs, -5 out of radiology
            context['from_labs'] = Patient.objects.filter(Q(status="-4") | Q(status="-45"))
            context['prev_visit'] = patientVisit.objects.filter(Q(patient_no=self.kwargs['patient_no']))
            # print(context['prev_visit'])
            context['from_radiology'] = Patient.objects.filter(Q(status="-5") | Q(status="-54"))
            context['patient'] = patient_object

        except:
            raise Http404('Requested user not found.')


        return context


# Populate database for diagnosis ICD10
#
#
# for disease in icd10:
#     new_disease = Diagnosis.objects.create(name=disease['name'], code=disease['code'])
#     new_disease.save

