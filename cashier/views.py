from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import PatientBill
from billing.models import Billing
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import PatientBillform



class PatientBill(CreateView):
    model = PatientBill
    form_class = PatientBillform



    def get(self,request):
        form=PatientBillform();


        return render(request,'cashier/patientbill.html',{'form':form})









