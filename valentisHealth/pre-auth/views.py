from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import pre_auth
from .forms import pre_authForm


class pre_authListView(ListView):
    model = pre_auth


class pre_authCreateView(CreateView):
    model = pre_auth
    form_class = pre_authForm


class pre_authDetailView(DetailView):
    model = pre_auth


class pre_authUpdateView(UpdateView):
    model = pre_auth
    form_class = pre_authForm

