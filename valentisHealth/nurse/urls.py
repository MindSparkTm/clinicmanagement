from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'models', api.modelsViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for models
    url(r'^models/$', views.modelsListView.as_view(), name='nurse_triage_list'),
    url(r'^models/create/$', views.modelsCreateView.as_view(), name='nurse_triage_create'),
    url(r'^models/detail/(?P<slug>\S+)/$', views.modelsDetailView.as_view(), name='nurse_triage_detail'),
    url(r'^models/update/(?P<slug>\S+)/$', views.modelsUpdateView.as_view(), name='nurse_triage_update'),
)

