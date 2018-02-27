from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'labs', api.labsViewSet)
router.register(r'radiology', api.radiologyViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for labs
    url(r'^$', views.labsListView.as_view(), name='labs_list'),
    url(r'^create/$', views.labsCreateView.as_view(), name='labs_labs_create'),
    url(r'^detail/(?P<slug>\S+)/$', views.labsDetailView.as_view(), name='labs_labs_detail'),
    url(r'^update/(?P<slug>\S+)/$', views.labsUpdateView.as_view(), name='labs_labs_update'),
)

urlpatterns += (
    # urls for radiology
    url(r'^radiology/$', views.radiologyListView.as_view(), name='pythonradiology_list'),
    url(r'^radiology/create/$', views.radiologyCreateView.as_view(), name='labs_radiology_create'),
    url(r'^radiology/detail/(?P<slug>\S+)/$', views.radiologyDetailView.as_view(), name='labs_radiology_detail'),
    url(r'^radiology/update/(?P<slug>\S+)/$', views.radiologyUpdateView.as_view(), name='labs_radiology_update'),
)

urlpatterns += (
    # urls for RadiologyResult
    url(r'^radiologyresult/$', views.RadiologyResultListView.as_view(), name='radiologyresult_list'),
    url(r'^radiologyresult/new/(?P<patient_no>\S+)/$', views.RadiologyVisitView.as_view(), name='radiologyresult_create'),
    url(r'^radiologyresult/detail/(?P<slug>\S+)/$', views.RadiologyResultDetailView.as_view(), name='radiologyresult_detail'),
    url(r'^radiologyresult/update/(?P<slug>\S+)/$', views.RadiologyResultUpdateView.as_view(), name='radiologyresult_update'),
)

urlpatterns += (
    # urls for LabResults
    url(r'^labresults/$', views.LabResultsListView.as_view(), name='labresults_list'),
    url(r'^tests/(?P<triage_id>\S+)/$', views.Tests.as_view(), name='labresults_list'),
    url(r'^labs/(?P<patient_no>\S+)/$', views.LabsVisitView.as_view(), name='labresults_create'),
    url(r'^labresults/detail/(?P<slug>\S+)/$', views.LabResultsDetailView.as_view(), name='labresults_detail'),
    url(r'^labresults/update/(?P<slug>\S+)/$', views.LabResultsUpdateView.as_view(), name='labresults_update'),
)