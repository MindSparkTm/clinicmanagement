from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import member_info, member_benefits, member_anniversary, member_acceptance, principal_applicant, pre_authorization, provider, cash
from .forms import member_infoForm, member_benefitsForm, member_anniversaryForm, member_acceptanceForm, principal_applicantForm, pre_authorizationForm, providerForm, cashForm
from rest_framework import generics
from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import serializers
from django.template.loader import get_template
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from xhtml2pdf import pisa
import json
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import UserPassesTestMixin
from valentisHealth.authenticator import *

class member_infoListView(UserPassesTestMixin, ListView):
    model = member_info

    def test_func(self):
        return is_callcenter(self)


class member_infoCreateView(UserPassesTestMixin, CreateView):
    model = member_info
    form_class = member_infoForm

    def test_func(self):
        return is_callcenter(self)


class member_infoDetailView(UserPassesTestMixin, DetailView):
    model = member_info

    def test_func(self):
        return is_callcenter(self)


class member_infoUpdateView(UserPassesTestMixin, UpdateView):
    model = member_info
    form_class = member_infoForm

    def test_func(self):
        return is_callcenter(self)


class member_benefitsListView(UserPassesTestMixin, ListView):
    model = member_benefits

    def test_func(self):
        return is_callcenter(self)


class member_benefitsCreateView(UserPassesTestMixin, CreateView):
    model = member_benefits
    form_class = member_benefitsForm

    def test_func(self):
        return is_callcenter(self)


class member_benefitsDetailView(UserPassesTestMixin, DetailView):
    model = member_benefits

    def test_func(self):
        return is_callcenter(self)


class member_benefitsUpdateView(UserPassesTestMixin, UpdateView):
    model = member_benefits
    form_class = member_benefitsForm

    def test_func(self):
        return is_callcenter(self)


class member_anniversaryListView(UserPassesTestMixin, ListView):
    model = member_anniversary

    def test_func(self):
        return is_callcenter(self)


class member_anniversaryCreateView(CreateView):
    model = member_anniversary
    form_class = member_anniversaryForm


class member_anniversaryDetailView(DetailView):
    model = member_anniversary


class member_anniversaryUpdateView(UpdateView):
    model = member_anniversary
    form_class = member_anniversaryForm


class member_acceptanceListView(ListView):
    model = member_acceptance


class member_acceptanceCreateView(CreateView):
    model = member_acceptance
    form_class = member_acceptanceForm


class member_acceptanceDetailView(DetailView):
    model = member_acceptance


class member_acceptanceUpdateView(UpdateView):
    model = member_acceptance
    form_class = member_acceptanceForm


class principal_applicantListView(ListView):
    model = principal_applicant


class principal_applicantCreateView(CreateView):
    model = principal_applicant
    form_class = principal_applicantForm


class principal_applicantDetailView(DetailView):
    model = principal_applicant


class principal_applicantUpdateView(UpdateView):
    model = principal_applicant
    form_class = principal_applicantForm


class pre_authorizationListView(UserPassesTestMixin, ListView):
    model = pre_authorization

    def test_func(self):
        return is_callcenter(self)


class AjaxPreAuthorizationSearch(UserPassesTestMixin, View):
    def test_func(self):
        return is_callcenter(self)

    def get(self, request):
        if request.is_ajax():
            q = request.GET.get('q', '')
            members = member_info.objects.filter(Q(first_name__icontains=q)| Q(surname__icontains=q)
                                                 | Q(other_name__icontains=q)| Q(member_no__icontains=q) |
                                                 Q(passport_no__icontains=q))[:20]
            results = []
            for member in members:
                member_json = dict()
                member_json['member_no'] = member.member_no
                member_json['surname'] = member.surname
                member_json['first_name'] = member.first_name
                member_json['other_name'] = member.other_name
                member_json['user_id'] = member.user_id
                member_json['gender'] = int(member.gender)
                member_json['passport_no'] = member.passport_no
                results.append(member_json)
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)


class PreAuthorizationSearch(UserPassesTestMixin, View):
    def test_func(self):
        return is_callcenter(self)

    def get(self, request):
        return render(request, 'payments/search_member_info.html', {})


class PreAuthorizationCreateView(UserPassesTestMixin, View):
    def test_func(self):
        return is_callcenter(self)

    def get(self, request, slug):
        member = get_object_or_404(member_info, member_no=slug)
        form = pre_authorizationForm()
        status = member.is_active()
        if not status:
            messages.error(request, 'The member is not active')

        d = {
            'form': form,
            'member': member
        }
        return render(request, 'payments/pre_authorization_form.1.html', d)

    def post(self, request, slug):
        form = pre_authorizationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            member_no = instance.member_no
            print(member_no)
            anniversary = member_anniversary.objects.filter(member_no=member_no).first()
            if anniversary:
                instance.anniv = anniversary.anniv
            instance.save()
            return redirect(reverse('payments_pre_authorization_print', kwargs={'slug': instance.slug}))
        else:
            print('failed!')
            print(form.errors)
            member = get_object_or_404(member_info, member_no=slug)
            # form = pre_authorizationForm()
            print(form.errors)
            d = {
                'form': form,
                'member': member
            }
            return render(request, 'payments/pre_authorization_form.1.html', d)


class PPreAuthorizationCreateView(UserPassesTestMixin, View):
    def test_func(self):
        return is_callcenter(self)

    def get(self, request, slug):
        member = get_object_or_404(member_info, member_no=slug)
        form = pre_authorizationForm()
        status = member.is_active()
        if not status:
            messages.error(request, 'The member is not active')
        d = {
            'form': form,
            'member': member
        }
        return render(request, 'payments/pre_authorization_form.2.html', d)

    def post(self, request, slug):
        form = pre_authorizationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            member_no = instance.member_no
            print(member_no)
            anniversary = member_anniversary.objects.filter(member_no=member_no).first()
            if anniversary:
                instance.anniv = anniversary.anniv
            instance.save()
            return redirect(reverse('payments_pre_authorization_print', kwargs={'slug': instance.slug}))
        else:
            print('failed!')
            print(form.errors)
            member = get_object_or_404(member_info, member_no=slug)
            # form = pre_authorizationForm()
            print(form.errors)
            d = {
                'form': form,
                'member': member
            }
            return render(request, 'payments/pre_authorization_form.2.html', d)


class pre_authorizationCreateView(UserPassesTestMixin, CreateView):
    model = pre_authorization
    form_class = pre_authorizationForm

class pre_authorform:

    def get_template_names(self):
        return 'payments/preauthsform.html'

    form_class = pre_authorizationForm

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        member_id = self.kwargs['member_id']
        try:
            benefits = member_benefits.objects.filter(slug__icontains=member_id)
            print(benefits)
            return benefits
        except:
            print(404)
            raise Http404('Requested user not found.')



class pre_authorizationDetailView(UserPassesTestMixin, DetailView):
    model = pre_authorization


def render_to_pdf(template_src, context_dict, action='view'):
    template = get_template(template_src)
    context = context_dict
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Authorization.pdf"'

    pisaStatus = pisa.CreatePDF(
        html, dest=response)

    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    else:
        return response


class PreAuthorizationPrintView(UserPassesTestMixin, View):
    def get(self, request, slug):
        print(slug)
        pre_auth = get_object_or_404(pre_authorization, slug=slug)
        d = {
            'pagesize': 'A4',
            'pre_auth': pre_auth,
            'user': request.user,
            # 'reference_no': pre_auth.slug,
            # 'date': pre_auth.date_authorized,
            # 'no_of_days': pre_auth.admit_days,
            # 'ward': pre_auth.ward,
            # 'provider': pre_auth.provider,
            # 'days_bed_charges': pre_auth.day_bed_charge ,
            # 'authority_type': pre_auth.authority_type,
            # 're': pre_auth.name,
            # 'member_no': pre_auth.member_no,
            # 'corporate': 'none',
            'notes': pre_auth.notes

        }
        return render_to_pdf('pre_authorization_pdf.html', d)


class pre_authorizationUpdateView(UpdateView):
    model = pre_authorization
    form_class = pre_authorizationForm


class providerListView(ListView):
    model = provider


class providerCreateView(CreateView):
    model = provider
    form_class = providerForm


class providerDetailView(DetailView):
    model = provider


class providerUpdateView(UpdateView):
    model = provider
    form_class = providerForm


class cashListView(ListView):
    model = cash


class cashCreateView(CreateView):
    model = cash
    form_class = cashForm


class cashDetailView(DetailView):
    model = cash


class cashUpdateView(UpdateView):
    model = cash
    form_class = cashForm

class getUser(generics.ListAPIView):
    serializer_class = serializers.member_infoSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        member_id = self.kwargs['member_id']
        print(member_id)
        try:
            user = member_info.objects.filter(slug=member_id)
            return user
        except:
            raise Http404('Requested user not found.')

class getBenefits(generics.ListAPIView):
    serializer_class = serializers.member_benefitsSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        member_id = self.kwargs['member_id']
        print(member_id)
        try:
            user = member_benefits.objects.filter(slug__icontains=member_id)
            return user
        except:
            raise Http404('Requested user not found.')

class getAniversary(generics.ListAPIView):
    serializer_class = serializers.member_anniversarySerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        member_id = self.kwargs['member_id']
        print(member_id)
        try:
            user = member_anniversary.objects.all().filter(slug=member_id)
            return user
        except:
            raise Http404('Requested user not found.')


class UpdateLimit(generics.UpdateAPIView):
    queryset = member_benefits.objects.all()
    serializer_class = serializers.member_benefitsSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        instance = self.get_object()
        instance.name = request.data.get("limit")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return serializer.data