from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^log-in/$', LoginPage.as_view(), name='login'),
    url(r'^pdf/', print_pdf, name='print'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^admin/adduser/', AddUser.as_view(), name='adduser'),
    # url(r'^admin/', Admin.as_view(), name='admin'),


]