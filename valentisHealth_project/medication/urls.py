from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'models', api.modelsViewSet)
router.register(r'MyDawa', api.myDawaModelSet)
router.register(r'MyDawaPrescriptions', api.myDawaPrescriptionsModelSet)



urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
    #url(r'^api/v2/', include(router.urls)),

)

urlpatterns += (
    # urls for models
    url(r'^models/$', views.modelsListView.as_view(), name='medication_models_list'),
    url(r'^search/$', views.ModelSearchView.as_view(), name='medication_models_search'),
    url(r'^models/new/(?P<patient_no>\S+)/$', views.modelsCreateView.as_view(), name='medication_models_create'),
    url(r'^models/detail/(?P<slug>\S+)/$', views.modelsDetailView.as_view(), name='medication_models_detail'),
    url(r'^models/update/(?P<slug>\S+)/$', views.modelsUpdateView.as_view(), name='medication_models_update'),
)

