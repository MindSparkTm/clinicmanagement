from django.conf.urls import url, include
from rest_framework import routers
from . import views,api

router = routers.DefaultRouter()
router.register(r'cashierservice', api.Cashierservice)







urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for patientVisit
    url(r'^patientbill/$', views.patientBill.as_view(), name='patientbill'),
    url(r'^invoicepdf/$', views.invoicepdf.as_view(), name='invoicepdf'),
    url(r'^patientbill/invoicepdf/$', views.invoicepdf.as_view(), name='invoicepdf'),
    url(r'^patientbill/invoice/$', views.invoice.as_view(), name='invoice'),

)

