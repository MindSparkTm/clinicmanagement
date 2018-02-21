from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import patientVisit, Diagnosis
from .forms import patientVisitForm
from registration.models import models as Patient
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from nurse.models import models as Triage
from django.db.models import Q
from rest_framework import generics
from labs.serializers import LabResultsSerializer, RadiologyResultSerializer
from labs.models import Labs, Radiology, RadiologyResult, LabResults
from labs.forms import labsForm, radiologyForm, RadiologyResultForm, LabResultsForm
from django.forms.models import model_to_dict
from medication.models import models as Medication

class patientVisitListView(ListView):
    model = patientVisit

    def get_template_names(self):
        if self.request.user.groups.filter(name='Doctor').exists():
            return 'clinic/visitform_list.html'
        else:
            raise Http404('Requested user not found.')

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
        if self.request.user.groups.filter(name='Doctor').exists():
            return 'clinic/visitform_copy.html'
        else:
            raise Http404('Requested user not found.')


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
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])

        try:
            labresult = LabResults.objects.filter(triage_id=patient_object.session_id)
            labtest = Labs.objects.filter(triage_id=patient_object.session_id).latest('created')
            context['lab_results'] = labresult
            context['lab_tests'] = labsForm(data=model_to_dict(labtest))

        except:
            pass

        try:
            radiologyresult = RadiologyResult.objects.filter(triage_id=patient_object.session_id)
            radiologytest = Radiology.objects.filter(triage_id=patient_object.session_id).latest('created')
            context['radiology_results'] = radiologyresult
            context['radiology_test'] = radiologyForm(data=model_to_dict(radiologytest))
        except:
            pass

        try:
            context['triage'] = Triage.objects.filter(patient_no=self.kwargs['patient_no'])[0]
            patient_object.session_id = context['triage'].triage_id
            patient_object.save()

        except:
            context['triage'] = Triage.objects.filter(patient_no=self.kwargs['patient_no'])
            patient_object.session_id = context['triage'].triage_id
            patient_object.save()

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


class ClinicReport(ListView):
    model = patientVisit

    def get_template_names(self):
        return 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ClinicReport, self).get_context_data(**kwargs)

        try:
            visit_obj = patientVisit.objects.get(visit_id=self.kwargs['visit_id'])
            context['visit'] = visit_obj
        except:
            pass
        try:
            patient_object = Patient.objects.get(patient_no=visit_obj.patient_no)
            context['patient'] = patient_object
        except:
            pass
        try:
            prescription = Medication.objects.get(triage_id=visit_obj.triage_id)
            context['prescription'] = prescription
        except:
            pass
        try:
            triage = Triage.objects.get(triage_id=visit_obj.triage_id)
            context['triage'] = triage
        except:
            pass

        return context
# Populate database for diagnosis ICD10

# for disease in icd10:
#     new_disease = Diagnosis.objects.create(name=disease['name'], code=disease['code'])
#     new_disease.save
#
