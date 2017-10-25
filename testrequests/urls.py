from django.conf.urls import url

from . import views

urlpatterns = [
    url('^create/department/$', views.DepartmentCreateView.as_view(), name='department'),
    url('^create/employee/$', views.EmployeeCreateView.as_view(), name='employee'),
    url('^create/customer/$', views.CustomerCreateView.as_view(), name='customer'),
    url('^create/test-type/$', views.TestTypeCreateView.as_view(), name='test_type'),
    url('^create/$', views.TestCreateView.as_view(), name='create'),
    url('^edit/(?P<pk>\d+)/$', views.TestUpdateView.as_view(), name='update'),
    url('^delete/(?P<pk>\d+)/$', views.TestDeleteView.as_view(), name='delete'),
    url('^$', views.TestListView.as_view(), name='list'),
]