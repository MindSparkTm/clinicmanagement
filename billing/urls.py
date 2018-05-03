from django.conf.urls import url, include
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()

router.register(r'billingservice', api.BillingService)






urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit
    url(r'^service/$', views.Billinginfo.as_view(), name='Billinginfo'),

)

