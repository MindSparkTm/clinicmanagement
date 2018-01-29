from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import models
from .forms import modelsForm
from registration.models import models as Patient
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404

class modelsListView(ListView):
    model = models


class modelsCreateView(CreateView):
    model = models
    form_class = modelsForm

    def get_context_data(self, **kwargs):
        context = super(modelsCreateView, self).get_context_data(**kwargs)

        context['waiting_list'] = Patient.objects.filter(status__icontains="2")
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_id=form.cleaned_data['patient_id'])
            patient_object.status = 3
            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/nurse/models/create/?sucess=true")



class modelsDetailView(DetailView):
    model = models


class modelsUpdateView(UpdateView):
    model = models
    form_class = modelsForm

