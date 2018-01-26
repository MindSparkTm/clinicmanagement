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
    url(r'^registration/models/$', views.modelsListView.as_view(), name='registration_models_list'),
    url(r'^registration/models/create/$', views.modelsCreateView.as_view(), name='registration_models_create'),
    url(r'^registration/models/detail/(?P<pk>\S+)/$', views.modelsDetailView.as_view(), name='registration_models_detail'),
    url(r'^registration/models/update/(?P<pk>\S+)/$', views.modelsUpdateView.as_view(), name='registration_models_update'),
)

