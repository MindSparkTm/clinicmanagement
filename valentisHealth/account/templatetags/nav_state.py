__author__ = 'Hp'
from django.core.urlresolvers import resolve
from django.template import Library
from django.contrib.auth.models import Group
from valentisHealth.authenticator import *

register = Library()


@register.simple_tag
def nav_active(request, url):
    """
    In template: {% nav_active request "url_name_here" %}
    """
    url_name = resolve(request.path).url_name
    if url_name == url:
        return "active"
    return ""


@register.simple_tag
def current_route(request):
    current_url = resolve(request.path_info).url_name
    return current_url

    # nav_active() will check the web request url_name and compare it
    # to the named url group within urls.py,
    # setting the active class if they match.


@register.simple_tag()
def has_group(request):

    all_links = {
        "registration": """<a href="/registration/" class='"""+nav_active(request,"registration_search")+"""' ><i class="fa fa-user-plus spav"> </i> Registration   </a>""",
        "triage": """<a href="/nurse/models/create/"  class='"""+nav_active(request,"nurse_models_create")+"""' > <i class="fa fa-address-book spav"> </i>  Triage  </a>""",
        "clinic": """<a href="/clinic/patientvisit/create/"  class="{% nav_active request 'clinic_patientvisit_create' %}"  > <i class="fa fa-clipboard spav"> </i> Clinic</a>""",
        "labs": """<a href="/labs/" class="{% nav_active request 'labs_labs_list' %}"> <i class="fa fa-flask spav"> </i>  Labs  </a>""",
        "radiology": """<a href="/labs/radiology/" class="{% nav_active request 'labs_radiology_list' %}"> <i class="fa fa-bolt spav"> </i> Radiology </a>""",
        "prescription": """<a href="/medication/search/" class="{% nav_active request 'medication_models_search' %}"> <i class="fa fa-book spav"> </i> Prescriptions </a>""",
        "payments": """<a href="/payments/search_member/" class="{% nav_active request 'payments_pre_authorization_search' %}"> <i class="fa fa-book spav"> </i> Authorization </a>""",
        }

    if is_admin(request):
        return [all_links[link] for link in all_links.keys() if link not in ['clinic']]

    if is_doctor(register):
        return "".join([all_links[link] for link in all_links.keys() if link not in ['payments']])

    if is_nurse(register):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'clinic', 'radiology', 'labs', 'prescriptions']])

    if is_labs(register):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'clinic', 'radiology', 'triage', 'prescriptions']])

    if is_radiology(register):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'clinic', 'triage', 'labs', 'prescriptions']])

    if is_callcenter(register):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'triage', 'clinic', 'radiology', 'labs', 'prescriptions']])

    if is_superadmin(register):
        return "".join([all_links[link] for link in all_links.keys()])

        # return is_admin(request)
