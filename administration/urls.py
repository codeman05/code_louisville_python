from django.conf.urls import url

from . import views

urlpatterns = [

    ########################################################################
    #                                                                      #
    # Create URL's                                                         #
    #                                                                      #
    ########################################################################

    url(r'^employee/create/$', views.CreateEmployeeView.as_view(), name='employee'),
    url(r'^department/create/$', views.CreateDepartmentView.as_view(), name='department'),
    url(r'^customer/create/$', views.CreateCustomerView.as_view(), name='customer'),
    url(r'^test-type/create/$', views.CreateTestTypeView.as_view(), name='test_type'),
    url('^test-request/create/$', views.TestCreateView.as_view(), name='test_request'),

    ########################################################################
    #                                                                      #
    # List (Read) URL's                                                    #
    #                                                                      #
    ########################################################################

    url(r'employee/list/$', views.EmployeeListView.as_view(), name='employee_list'),
    url(r'department/list/$', views.DepartmentListView.as_view(), name='department_list'),
    url(r'customer/list/$', views.CustomerListView.as_view(), name='customer_list'),
    url(r'test-type/list/$', views.TestTypeListView.as_view(), name='test_type_list'),
    url('^test-request/list/$', views.TestListView.as_view(), name='test_request_list'),


    ########################################################################
    #                                                                      #
    # Edit (Update) URL's                                                  #
    #                                                                      #
    ########################################################################

    url(r'employee/update/(?P<pk>\d+)/$', views.EmployeeUpdateView.as_view(), name='update_employee'),
    url(r'department/update/(?P<pk>\d+)/$', views.DepartmentUpdateView.as_view(), name='update_department'),
    url(r'customer/update/(?P<pk>\d+)/$', views.CustomerUpdateView.as_view(), name='update_customer'),
    url(r'test-type/update/(?P<pk>\d+)/$', views.TestTypeUpdateView.as_view(), name='update_test_type'),
    url(r'test-request/update/(?P<pk>\d+)/$', views.TestUpdateView.as_view(), name='update_test_request'),

    ########################################################################
    #                                                                      #
    # Delete URL's                                                         #
    #                                                                      #
    ########################################################################

    url(r'employee/delete/(?P<pk>\d+)/$', views.DeleteEmployeeView.as_view(), name='delete_employee'),
    url(r'department/delete/(?P<pk>\d+)/$', views.DeleteDepartmentView.as_view(), name='delete_department'),
    url(r'customer/delete/(?P<pk>\d+)/$', views.DeleteCustomerView.as_view(), name='delete_customer'),
    url(r'test-type/delete/(?P<pk>\d+)/$', views.DeleteTestTypeView.as_view(), name='delete_test_type'),
    url('^test-request/delete/(?P<pk>\d+)/$', views.TestDeleteView.as_view(), name='delete_test_request'),
]