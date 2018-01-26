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
    url(r'^clinic/models/$', views.modelsListView.as_view(), name='clinic_models_list'),
    url(r'^clinic/models/create/$', views.modelsCreateView.as_view(), name='clinic_models_create'),
    url(r'^clinic/models/detail/(?P<slug>\S+)/$', views.modelsDetailView.as_view(), name='clinic_models_detail'),
    url(r'^clinic/models/update/(?P<slug>\S+)/$', views.modelsUpdateView.as_view(), name='clinic_models_update'),
)

