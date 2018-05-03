from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Billing
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import Billingform



class Billinginfo(CreateView):
    model = Billing
    form_class = Billingform



    def get(self,request):
        form=Billingform();
        return render(request,'billing/billingform.html',{'form':form})

    def form_valid(self, form):
        user_service = form.cleaned_data.get('service')
        user_price = form.cleaned_data.get('price')
        servicedetails = Billing(service=user_service, price=user_price)
        servicedetails.save()

        print('user service',user_service)
        return redirect('Billinginfo')





