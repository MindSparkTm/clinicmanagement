from django.shortcuts import render
from django.views.generic import View, CreateView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, reverse
from django.contrib import messages
from urllib.parse import urlencode
from valentisHealth.authenticator import *
from .models import CustomUser
from .forms import CustomUserForm
from io import StringIO
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from xhtml2pdf import pisa
from django.utils.html import escape
from django.conf import settings
from django.contrib.auth.models import Group
from .forms import LoginForm
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token


class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html', {})

class Workflow(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'workflow.html', {})

class AddUser(CreateView):
    model = CustomUser
    form_class = CustomUserForm

    def test_func(self):
        return is_admin(request)

    def get_template_names(self):
        return 'addmember.html'

    def form_valid(self, form):
        print("+++++++++++++++++++++++++++form_valid adduser+++++++++++++")
        instance = form.save(commit=False)
        instance.save()

        user_group = Group.objects.get(name=form.cleaned_data['role'])
        user_group.user_set.add(instance)

        instance.send_confirmation(self.request)

        return render(self.request, 'addmember.html', {'success':"Successful"})


# class AccountAcctivation(View):
def activate(request, email, token):
    try:
        # email = force_text(urlsafe_base64_decode(email))
        user = CustomUser.objects.get(email=email)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.activate(request)

        return render(request, 'success.html', {'user':user})
    else:
        return HttpResponse('Activation link is invalid!')


class LoginPage(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=request.POST['email_address'],
                                    password=request.POST['password'])

                if user is not None:
                    if user.is_active and not user.is_patient:
                        login(request, user)
                        if 'next' in request.GET:
                            params = request.GET.copy()
                            del params['next']
                            return redirect(request.GET.get('next') + '?' + urlencode(params))
                        else:
                            return redirect(reverse('registration_search'))
                            # return redirect("/")
                    else:
                        message = "You need to activate your account first before you can sign in."
                        messages.error(request, message)
                        return render(request, "login.html", {'form': form})

                else:
                    message = "Invalid email address or password"
                    messages.error(request, message)
                    return render(request, "login.html", {'form': form})
        else:
            form = LoginForm()
        return render(request, "login.html", {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


def render_to_pdf(template_src, context_dict, action='view'):
    template = get_template(template_src)
    context = context_dict
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Authoriza.pdf"'

    pisaStatus = pisa.CreatePDF(
        html, dest=response)

    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    else:
        return response


def print_pdf(request):
    d = {
        'pagesize': 'A4',
        'supplier': '',
        'item_details': '',
        'lpo': '',
        'site_name': 'name'
    }
    return render_to_pdf('pdf.html', d)


