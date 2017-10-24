from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.TestListView.as_view(), name='list'),
    url('^(?P<pk>\d+)/$', views.TestDetailView.as_view(), name='detail'),
]