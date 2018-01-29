from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import models
from .forms import modelsForm
from django.http import HttpResponseRedirect

class modelsListView(ListView):
    model = models


class modelsCreateView(CreateView):
    model = models
    form_class = modelsForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status = 2
        # if (instance.status >= 0):
        #      instance.season -= 1
        # else:
        #     instance.season = 0

        instance.save()
        print(instance.status)

        return HttpResponseRedirect("")


class modelsDetailView(DetailView):
    model = models


class modelsUpdateView(UpdateView):
    model = models
    form_class = modelsForm

