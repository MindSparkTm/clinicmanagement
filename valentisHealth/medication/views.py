from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import models
from .forms import modelsForm


class modelsListView(ListView):
    model = models


class modelsCreateView(CreateView):
    model = models
    form_class = modelsForm


class modelsDetailView(DetailView):
    model = models


class modelsUpdateView(UpdateView):
    model = models
    form_class = modelsForm

