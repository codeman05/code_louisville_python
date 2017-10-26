from django.conf.urls import url

from . import views

urlpatterns = [
    url('^create/test-request/$', views.TestCreateView.as_view(), name='create'),
    url('^update/test-request/(?P<pk>\d+)/$', views.TestUpdateView.as_view(), name='update'),
    url('^delete/test-request/(?P<pk>\d+)/$', views.TestDeleteView.as_view(), name='delete'),
    url('^list/test-request/$', views.TestListView.as_view(), name='list'),
]