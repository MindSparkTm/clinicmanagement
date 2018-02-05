from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Labs, Radiology, RadiologyResult, LabResults
from .forms import labsForm, radiologyForm, RadiologyResultForm, LabResultsForm
from django.http import HttpResponseRedirect
from registration.models import models as Patient
from django.http import HttpResponse, Http404
from django.shortcuts import render #, get_object_or_404, redirect, reverse

class labsListView(ListView):
    model = Labs

    def get_context_data(self, **kwargs):
        context = super(labsListView, self).get_context_data(**kwargs)

        try:
            #get patients in labs (status 4)
            context['waiting_list'] = Patient.objects.filter(status="4")
            context['show_waiting_list'] = True

            #sent linkt to be appended to the href in waiting list table row accounts/templates/base
            context['link'] = 'labs/labs'

        except:
            raise Http404('Requested user not found.')

        return context


class labsCreateView(CreateView):
    model = Labs
    form_class = labsForm

    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.attending_doc = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])
            # status 0 means patient's session ended
            patient_object.status = 4
            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        #status 4 means patient's in lab
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
        return 'labs/radiology_list.html'

    def get_context_data(self, **kwargs):
        context = super(radiologyListView, self).get_context_data(**kwargs)

        try:
            #get patient's in radiology (staus 5)
            context['waiting_list'] = Patient.objects.filter(status="5")

            context['show_waiting_list'] = True
            context['link'] = 'labs/radiology'
        except:
            raise Http404('Requested user not found.')

        return context


class radiologyCreateView(CreateView):
    model = Radiology
    form_class = radiologyForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        # status 5 means patient's in radiology
        instance.status = 5
        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")


class radiologyDetailView(DetailView):
    model = Radiology


class radiologyUpdateView(UpdateView):
    model = Radiology
    form_class = radiologyForm



class RadiologyResultListView(ListView):
    model = RadiologyResult


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
    form_class = LabResultsForm

    def get_template_names(self):
        return 'labs/labresult_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            #status 4 means patient in out of labs
            patient_object.status = -4
            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/labs/")

    def get_context_data(self, **kwargs):

        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        context = super(LabsVisitView, self).get_context_data(**kwargs)

        try:
            context['patient'] = patient_object

            patient_object.status = 4

        except:
            raise Http404('Requested user not found.')

        return context


class RadiologyVisitView(ListView):
    model = RadiologyResult
    form_class = RadiologyResultForm

    def get_template_names(self):
        return 'labs/radiology_result_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            # status 5 means patient is in radiology
            patient_object.status = -5
            patient_object.save()

        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/labs/radiology")

    def get_context_data(self, **kwargs):

        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        context = super(RadiologyVisitView, self).get_context_data(**kwargs)

        try:
            context['patient'] = patient_object

        except:
            raise Http404('Requested user not found.')

        return context