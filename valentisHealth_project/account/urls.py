from django.conf.urls import url

from .views import *
from rest_framework.authtoken import views
# from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    url('^log-in/$', LoginPage.as_view(), name='login'),
    url(r'^pdf/', print_pdf, name='print'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^admin/adduser/', AddUser.as_view(), name='adduser'),
    url(r'^activate/(?P<email>[0-9A-Za-z_@\-.]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^workflow', Workflow.as_view(), name='workflow'),
    # url(r'^admin/', Admin.as_view(), name='admin'),

]

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token),
    # url(r'^api-token-refresh/', refresh_jwt_token),
]