from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.TestListView.as_view(), name='list'),
    #url('^(?P<pk>\d+)/$', views.TestDetailView.as_view(), name='detail'),
    url('^create/', views.TestCreateView.as_view(), name='create'),
    url('^edit/(?P<pk>\d+)/$', views.TestUpdateView.as_view(), name='update'),
    url('^delete/(?P<pk>\d+)/$', views.TestDeleteView.as_view(), name='delete'),
]