__author__ = 'Stephen'
from django.core.urlresolvers import resolve
from django.template import Library
from valentisHealth.authenticator import *

register = Library()



def nav_active(request, url):
    """
    In template: {% nav_active request "url_name_here" %}
    """
    path_object = request.path.split('/')[:3]
    url_name = resolve(request.path).url_name
    # if url_name == url:
    #     return 'active'
    if url == 'labs':
        path_object = path_object[1:]

    if url in request.path.split('/')[:3]:
        return 'active'
    return ''


@register.simple_tag()
def has_group(request):

    all_links = {
        "registration": """<a href="/registration/" class=\""""+nav_active(request,"registration")+"""\"  ><i class="fa fa-user-plus spav"> </i> Registration   </a>""",

        "triage": """<a href="/nurse/models/create/"  class=\""""+nav_active(request,"nurse")+"""\" > <i class="fa fa-address-book spav"> </i>  Triage  </a>""",
        "clinic": """<a href="/clinic/patientvisit/create/"  class=\""""+nav_active(request,'clinic')+"""\"  > <i class="fa fa-clipboard spav"> </i> Clinic</a>""",
        "labs": """<a href="/labs/" class=\""""+nav_active(request,'labs')+"""\"> <i class="fa fa-flask spav"> </i>  Labs  </a>""",
        "radiology": """<a href="/labs/radiology/" class=\""""+nav_active(request,'radiology')+""""> <i class="fa fa-bolt spav"> </i> Radiology </a>""",
        "prescription": """<a href="/medication/search/" class=\""""+nav_active(request,'medication')+"""\"> <i class="fa fa-book spav"> </i> Prescriptions </a>""",
        "payments": """<a href="/payments/search_member/" class=\""""+nav_active(request,'payments')+""""> <i class="fa fa-book spav"> </i> Authorization </a>""",
        "admin": """<a href="/account/admin/adduser" class=\""""+nav_active(request,'account')+""""> <i class="fa fa-book spav"> </i> Admin </a>""",
        }

    if is_admin(request):
        return "".join([all_links[link] for link in all_links.keys()])

    if is_doctor(request):
        return "".join([all_links[link] for link in all_links.keys() if link not in ['payments', 'admin']])

    if is_nurse(request):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'clinic', 'radiology', 'labs', 'prescription', 'admin']])

    if is_labs(request):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'clinic', 'radiology', 'triage', 'prescription', 'admin']])

    if is_radiology(request):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'clinic', 'triage', 'labs', 'prescription', 'admin']])

    if is_callcenter(request):
        return "".join([all_links[link] for link in all_links.keys() ])

    if is_superadmin(request):
        return "".join([all_links[link] for link in all_links.keys()])

    if is_receptionist(request):
        return "".join([all_links[link] for link in all_links.keys() if
                        link not in ['payments', 'triage', 'clinic', 'radiology', 'labs', 'prescription', 'admin']])

        # return is_admin(request)
