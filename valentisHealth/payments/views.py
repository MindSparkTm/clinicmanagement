from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import member_info, member_benefits, member_anniversary, member_acceptance, principal_applicant, pre_authorization, provider, cash
from .forms import member_infoForm, member_benefitsForm, member_anniversaryForm, member_acceptanceForm, principal_applicantForm, pre_authorizationForm, providerForm, cashForm
from rest_framework import generics
from . import serializers

from django.http import HttpResponse, Http404

class member_infoListView(ListView):
    model = member_info


class member_infoCreateView(CreateView):
    model = member_info
    form_class = member_infoForm


class member_infoDetailView(DetailView):
    model = member_info


class member_infoUpdateView(UpdateView):
    model = member_info
    form_class = member_infoForm


class member_benefitsListView(ListView):
    model = member_benefits


class member_benefitsCreateView(CreateView):
    model = member_benefits
    form_class = member_benefitsForm


class member_benefitsDetailView(DetailView):
    model = member_benefits


class member_benefitsUpdateView(UpdateView):
    model = member_benefits
    form_class = member_benefitsForm


class member_anniversaryListView(ListView):
    model = member_anniversary


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


class pre_authorizationListView(ListView):
    model = pre_authorization

class searchView(ListView):
    # updatebenefit = member_benefitsUpdateView()
    model = pre_authorization
    def get_template_names(self):
        return 'payments/search_member.html'

class pre_authorizationCreateView(CreateView):
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



class pre_authorizationDetailView(DetailView):
    model = pre_authorization


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