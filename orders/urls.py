from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'list/', views.OrderList.as_view(), name='list'),
    url(r'create/$', views.create_order, name='create'),
    url(r'edit/(?P<order_pk>\d+)/$', views.edit_order, name='edit'),
    url(r'delete/(?P<order_pk>\d+)/$', views.delete_order, name='delete'),
]
