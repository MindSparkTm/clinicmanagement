from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Labs, Radiology, RadiologyResult, LabResults
from .forms import labsForm, radiologyForm, RadiologyResultForm, LabResultsForm
from django.http import HttpResponseRedirect, JsonResponse
from registration.models import models as Patient
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render #, get_object_or_404, redirect, reverse
from django.forms.models import model_to_dict
from django.db.models import Q
from rest_framework import generics
from .serializers import LabResultsSerializer, RadiologyResultSerializer

class labsListView(ListView):
    model = Labs

    def get_template_names(self):
        if self.request.user.groups.filter(Q(name='Doctor') | Q(name='Lab') | Q(name='Admin')).exists():
            return 'lab/labs_list.html'
        else:
            raise Http404('Requested user not found.')

    def get_context_data(self, **kwargs):
        context = super(labsListView, self).get_context_data(**kwargs)

        try:
            #get patients in labs (status 4)
            context['waiting_list'] = Patient.objects.filter(Q(status="4") | Q(status="45") | Q(status='-54'))
            context['show_waiting_list'] = True

            #sent linkt to be appended to the href in waiting list table row accounts/templates/base
            context['link'] = 'labs/labs'

        except:
            raise Http404('Requested user not found.')

        return context


class labsCreateView(CreateView):
    model = Labs
    form_class = labsForm

    def get_template_names(self):
        if self.request.user.groups.filter(Q(name='Doctor') | Q(name='Lab') | Q(name='Admin')).exists():
            return 'lab/labs_form.html'
        else:
            raise Http404('Requested user not found.')

    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.attending_doc = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            #if patient is in radiology
            if patient_object.status == 5:
                # 45 means patient is in both labs and Radiology
                patient_object.status = 45
            else:
                patient_object.status = 4

            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")


class labsDetailView(DetailView):
    model = Labs


class labsUpdateView(UpdateView):
    model = Labs
    form_class = labsForm


class radiologyListView(ListView):
    model = Radiology

    def get_template_names(self):
        if self.request.user.groups.filter(Q(name='Doctor') | Q(name='Lab') | Q(name='Admin')).exists():
            return 'labs/radiology_list.html'
        else:
            raise Http404('Requested user not found.')

    def get_context_data(self, **kwargs):
        context = super(radiologyListView, self).get_context_data(**kwargs)

        try:
            #get patient's in radiology (staus 5)
            context['waiting_list'] = Patient.objects.filter(Q(status="5") | Q(status="45") | Q(status="-45"))

            context['show_waiting_list'] = True
            context['link'] = 'labs/radiologyresult/new'
        except:
            raise Http404('Requested user not found.')

        return context


class radiologyCreateView(CreateView):
    model = Radiology
    form_class = radiologyForm

    def get_template_names(self):
        if self.request.user.groups.filter(Q(name='Doctor') | Q(name='Lab') | Q(name='Admin')).exists():
            return 'labs/radiology_form.html'
        else:
            raise Http404('Requested user not found.')

    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.attending_doc = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            # if patient is in labs
            if patient_object.status == 4:
                # 45 means patient is in both labs and Radiology
                patient_object.status = 45
            else:
                patient_object.status = 5

            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")


class radiologyDetailView(DetailView):
    model = Radiology


class radiologyUpdateView(UpdateView):
    model = Radiology
    form_class = radiologyForm



class RadiologyResultListView(ListView):
    model = RadiologyResult

    def get_template_names(self):
        if self.request.user.groups.filter(Q(name='Doctor') | Q(name='Lab') | Q(name='Admin')).exists():
            return ''
        else:
            raise Http404('Requested user not found.')


class RadiologyResultDetailView(DetailView):
    model = RadiologyResult


class RadiologyResultUpdateView(UpdateView):
    model = RadiologyResult
    form_class = RadiologyResultForm


class LabResultsListView(ListView):
    model = LabResults


class LabResultsDetailView(DetailView):
    model = LabResults


class LabResultsUpdateView(UpdateView):
    model = LabResults
    form_class = LabResultsForm


class LabsVisitView(CreateView):
    model = LabResults
    form_class = labsForm

    def get_template_names(self):
        return 'labs/labresult_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            print(form.cleaned_data['patient_no'])
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            #status -45 patient is out of labs but in radiology
            if patient_object.status==45:
                patient_object.status = -45

            else:
                #patient out of labs
                patient_object.status=-4

            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/labs/")

    def get_context_data(self, **kwargs):

        context = super(LabsVisitView, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            context['patient'] = patient_object
            lab_object = Labs.objects.filter(triage_id=patient_object.session_id).latest('created')
            object = labsForm(data=model_to_dict(lab_object))
            context['request_'] = object
            context['other'] = lab_object.other #text area field in the labresult form
            context['diagnosis'] = lab_object.diagnosis
        except:
            raise Http404('Requested user not found.')

        return context


class RadiologyVisitView(CreateView):
    model = RadiologyResult
    form_class = RadiologyResultForm

    def get_template_names(self):
        return 'labs/radiology_result_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            # status -54 patient is out of labs but in radiology
            if patient_object.status == 45:
                patient_object.status = -54
            else:
                # patient out of labs
                patient_object.status = -5

            patient_object.save()

        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/labs/radiology")

    def get_context_data(self, **kwargs):


        context = super(RadiologyVisitView, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            context['patient'] = patient_object
            radiology_object = Radiology.objects.filter(patient_no=self.kwargs['patient_no']).latest('created')

            object = radiologyForm(data=model_to_dict(radiology_object))
            context['request_'] = object
            context['examination'] =radiology_object.examination
            context['clinical_indication'] = radiology_object.clinical_indication
            # print(object)

        except:
            raise Http404('Requested user not found.')

        return context


def Tests(request, triage_id):
    return JsonResponse()

class Tests(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        labresult = LabResults.objects.filter(triage_id=kwargs.get('triage_id'))
        radiologyresult = RadiologyResult.objects.filter(triage_id=kwargs.get('triage_id'))

        context = {
            "request": request,
        }

        labs_serializer = LabResultsSerializer(labresult, many=True, context=context)
        radiology_serializer = RadiologyResultSerializer(radiologyresult, many=True, context=context)

        response = labs_serializer.data + radiology_serializer.data

        return JsonResponse(response)