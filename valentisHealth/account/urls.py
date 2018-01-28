from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^log-in/$', LoginPage.as_view(), name='login')
]