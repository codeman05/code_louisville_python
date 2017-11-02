########################################################################
#                                                                      #
# This is the configuration file for using django_tables2. A couple    #
# of global variables (attrs_setting) are used to stay DRY             #
#                                                                      #
########################################################################
import django_tables2 as tables
from django_tables2.utils import A

from . import models


attrs_setting = {'id': 'dataTable', 'class': 'table table-bordered', 'width': '100%', 'cellspacing': '0'}


class EmployeeTable(tables.Table):
    """Defines the attributes necessary to create the employee
    table used on the Employees Lists Page. The desire was to have a link that could
    allow editing or deleting a record.  The id field was chosen for this task.
    """

    first_name = tables.LinkColumn('administration:update_employee', args=[A('pk')])

    class Meta:
        model = models.Employee
        fields = (
            'first_name',
            'last_name',
            'department',
            'email',
        )
        attrs = attrs_setting


class DepartmentTable(tables.Table):
    """Defines the attributes necessary to create the department
    table used on the Departments Lists Page. The desire was to have a link that could
    allow editing or deleting a record.  The id field was chosen for this task.
    """

    name = tables.LinkColumn('administration:update_department', args=[A('pk')])

    class Meta:
        model = models.Department
        fields = (
            'name',
            'manager',
        )
        attrs = attrs_setting


class CustomerTable(tables.Table):
    """Defines the attributes necessary to create the customer
    table used on the Customers Lists Page. The desire was to have a link that could
    allow editing or deleting a record.  The id field was chosen for this task.
    """

    company = tables.LinkColumn('administration:update_customer', args=[A('pk')])

    class Meta:
        model = models.Customer
        fields = (
            'company',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
        )
        attrs = attrs_setting


class TestTypeTable(tables.Table):
    """ Defines the attributes necessary to create the test types
    table used on the Test Types Lists Page. The desire was to have a link that could
    allow editing or deleting a record.  The id field was chosen for this task.
    """

    name = tables.LinkColumn('administration:update_test_type', args=[A('pk')])

    class Meta:
        model = models.TestType
        fields = (
            'name',
            'code',
            'price',
            'department'
        )
        attrs = attrs_setting


class TestRequestsTable(tables.Table):
    """Defines the attributes necessary to create the Test Request Table
    used on the Test Requests Lists Page. The desire was to have a link that could
    allow editing or deleting a record.  The id field was chosen for this task.
    """

    id = tables.LinkColumn('administration:update_test_request', args=[A('pk')])

    customer = tables.LinkColumn('administration:customer_list')

    class Meta:
        model = models.Test
        fields = (
            'id',
            'customer',
            'test_type',
            'air_flow_rate',
            'manufacturer',
            'barcode_number',
            'location',
        )
        attrs = {'id': 'dataTable', 'class': 'table table-bordered', 'width': '100%', 'cellspacing': '0'}
