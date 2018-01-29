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
    url(r'^labs/$', views.labsListView.as_view(), name='labs_labs_list'),
    url(r'^labs/create/$', views.labsCreateView.as_view(), name='labs_labs_create'),
    url(r'^labs/detail/(?P<slug>\S+)/$', views.labsDetailView.as_view(), name='labs_labs_detail'),
    url(r'^labs/update/(?P<slug>\S+)/$', views.labsUpdateView.as_view(), name='labs_labs_update'),
)

urlpatterns += (
    # urls for radiology
    url(r'^radiology/$', views.radiologyListView.as_view(), name='labs_radiology_list'),
    url(r'^radiology/create/$', views.radiologyCreateView.as_view(), name='labs_radiology_create'),
    url(r'^radiology/detail/(?P<slug>\S+)/$', views.radiologyDetailView.as_view(), name='labs_radiology_detail'),
    url(r'^radiology/update/(?P<slug>\S+)/$', views.radiologyUpdateView.as_view(), name='labs_radiology_update'),
)

