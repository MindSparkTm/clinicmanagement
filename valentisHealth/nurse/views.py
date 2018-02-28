from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import models
from .forms import modelsForm
from registration.models import Patient
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import UserPassesTestMixin
from valentisHealth.authenticator import *

class modelsListView(ListView):
    model = models


class modelsCreateView(UserPassesTestMixin, CreateView):
    model = models
    form_class = modelsForm

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request)

    def get_context_data(self, **kwargs):
        context = super(modelsCreateView, self).get_context_data(**kwargs)

        context['waiting_list'] = Patient.objects.filter(status="2")
        # context['show_waiting_list'] = True
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])
            patient_object.status = 3
            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/nurse/models/create/?sucess=true")



class modelsDetailView(UserPassesTestMixin, DetailView):
    model = models

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request)


class modelsUpdateView(UserPassesTestMixin, UpdateView):
    model = models
    form_class = modelsForm

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request)

