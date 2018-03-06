from django.conf.urls import url

from .views import *

urlpatterns = [
    url('^log-in/$', LoginPage.as_view(), name='login'),
    url(r'^pdf/', print_pdf, name='print'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^admin/adduser/', AddUser.as_view(), name='adduser'),
    url(r'^activate/(?P<email>[0-9A-Za-z_@\-.]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    # url(r'^admin/', Admin.as_view(), name='admin'),


]