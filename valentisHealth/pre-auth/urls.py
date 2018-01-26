from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'pre_auth', api.pre_authViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for pre_auth
    url(r'^pre_auth/pre_auth/$', views.pre_authListView.as_view(), name='pre_auth_pre_auth_list'),
    url(r'^pre_auth/pre_auth/create/$', views.pre_authCreateView.as_view(), name='pre_auth_pre_auth_create'),
    url(r'^pre_auth/pre_auth/detail/(?P<slug>\S+)/$', views.pre_authDetailView.as_view(), name='pre_auth_pre_auth_detail'),
    url(r'^pre_auth/pre_auth/update/(?P<slug>\S+)/$', views.pre_authUpdateView.as_view(), name='pre_auth_pre_auth_update'),
)

