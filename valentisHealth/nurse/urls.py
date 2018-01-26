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
    url(r'^nurse/models/$', views.modelsListView.as_view(), name='nurse_models_list'),
    url(r'^nurse/models/create/$', views.modelsCreateView.as_view(), name='nurse_models_create'),
    url(r'^nurse/models/detail/(?P<slug>\S+)/$', views.modelsDetailView.as_view(), name='nurse_models_detail'),
    url(r'^nurse/models/update/(?P<slug>\S+)/$', views.modelsUpdateView.as_view(), name='nurse_models_update'),
)

