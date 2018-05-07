from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import PatientBill
from billing.models import Billing
from django.http import JsonResponse
from django.shortcuts import render,redirect
from .forms import PatientBillform
from django.http import Http404




class patientBill(CreateView):
    model = PatientBill
    form_class = PatientBillform



    def get(self,request):
        form=PatientBillform();


        return render(request,'cashier/patientbill.html',{'form':form})

    def form_valid(self,form):
        user_patientid = form.cleaned_data.get('patientid')
        user_totalbill = form.cleaned_data.get('totalbill')
        user_breakdown = form.cleaned_data.get('billbreakdown')
        user_invoiceid = form.cleaned_data.get('invoiceid')
        self.request.session['invoiceid'] = user_invoiceid
        self.request.session['patientid'] = user_patientid


        print('user_invoiceid',user_invoiceid)
        print ('user_breakdown',user_breakdown)
        print ('user_totalbill',user_totalbill)
        m_bill = PatientBill(patientid=user_patientid,totalbill=user_totalbill,billbreakdown=user_breakdown,invoiceid = user_invoiceid)
        m_bill.save()
        return redirect('invoicepdf')

class invoicepdf(CreateView):
    model = PatientBill
    form_class = PatientBillform



    def get_template_names(self):


        return 'cashier/invoice.html'

    def get_context_data(self, **kwargs):
        context = super(invoicepdf, self).get_context_data(**kwargs)
        _invoiceid = self.request.session['invoiceid']
        _patientid = self.request.session['patientid']
        print('lllkl',_invoiceid,_patientid)
        patient_object = {'patientid':_patientid,'invoiceid':_invoiceid}
        context['patient'] = patient_object
        return context

class invoice(CreateView):
    model = PatientBill
    form_class = PatientBillform

    def get(self,request):

        return render(request,'cashier/cashier_copy.html')














