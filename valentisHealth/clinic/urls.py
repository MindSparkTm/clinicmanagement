from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'patientvisit', api.patientVisitViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for patientVisit
    url(r'^patientvisit/$', views.patientVisitListView.as_view(), name='clinic_patientvisit_list'),
    url(r'^patientvisit/doctor/(?P<patient_id>\S+)/$', views.DoctorVisit.as_view(), name='docotor_visit'),
    url(r'^patientvisit/create/$', views.patientVisitCreateView.as_view(), name='clinic_patientvisit_create'),
    url(r'^patientvisit/detail/(?P<slug>\S+)/$', views.patientVisitDetailView.as_view(), name='clinic_patientvisit_detail'),
    url(r'^patientvisit/update/(?P<slug>\S+)/$', views.patientVisitUpdateView.as_view(), name='clinic_patientvisit_update'),
)

