from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'list/', views.order_list, name='list'),
    url(r'form/(?P<order_pk>[0-9]{1})/', views.order_detail, name='detail'),
    url(r'form/', views.order_form, name='form'),

]