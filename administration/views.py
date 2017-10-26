from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django_tables2 import RequestConfig


from . import models
from . import tables


########################################################################
#                                                                      #
# Create Views                                                         #
#                                                                      #
########################################################################


class CreateEmployeeView(CreateView):
    model = models.Employee
    template_name = 'administration/create_update_template.html'
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'department',
    )


class CreateDepartmentView(CreateView):
    model = models.Department
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'manager',
    )


class CreateCustomerView(CreateView):
    model = models.Customer
    template_name = 'administration/create_update_template.html'
    fields = (
        'company',
        'first_name',
        'last_name',
        'email',
        'address',
        'phone',
    )


class CreateTestTypeView(CreateView):
    model = models.TestType
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'code',
        'price',
        'department',
    )


########################################################################
#                                                                      #
# List (Read) Views                                                    #
#                                                                      #
########################################################################


class EmployeeListView(ListView):
    model = models.Employee
    template_name = 'administration/list_view_template.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        table = tables.EmployeeTable(models.Employee.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class DepartmentListView(ListView):
    model = models.Department
    template_name = 'administration/list_view_template.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        table = tables.DepartmentTable(models.Department.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class CustomerListView(ListView):
    model = models.Customer
    template_name = 'administration/list_view_template.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        table = tables.CustomerTable(models.Customer.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class TestTypeListView(ListView):
    model = models.TestType
    template_name = 'administration/list_view_template.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(TestTypeListView, self).get_context_data(**kwargs)
        table = tables.TestTypeTable(models.TestType.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


########################################################################
#                                                                      #
# Update Views                                                         #
#                                                                      #
########################################################################


class EmployeeUpdateView(UpdateView):
    model = models.Employee
    template_name = 'administration/create_update_template.html'
    context_object_name = 'object_list'
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'department',
    )


class DepartmentUpdateView(UpdateView):
    model = models.Department
    template_name = 'administration/create_update_template.html'
    context_object_name = 'object_list'
    fields = (
        'name',
        'manager',
    )


class CustomerUpdateView(UpdateView):
    model = models.Customer
    template_name = 'administration/create_update_template.html'
    context_object_name = 'object_list'
    fields = (
        'company',
        'first_name',
        'last_name',
        'email',
        'address',
        'phone',
    )


class TestTypeUpdateView(UpdateView):
    model = models.TestType
    template_name = 'administration/create_update_template.html'
    context_object_name = 'object_list'
    fields = (
        'name',
        'code',
        'price',
        'department',
    )


########################################################################
#                                                                      #
# Delete Views                                                         #
#                                                                      #
########################################################################


class DeleteEmployeeView(DeleteView):
    model = models.Employee
    template_name = 'test_confirm_delete.html'
    success_url = reverse_lazy('administration:employee_list')


class DeleteDepartmentView(DeleteView):
    model = models.Department
    template_name = 'test_confirm_delete.html'
    success_url = reverse_lazy('administration:department_list')


class DeleteCustomerView(DeleteView):
    model = models.Customer
    template_name = 'test_confirm_delete.html'
    success_url = reverse_lazy('administration:customer_list')


class DeleteTestTypeView(DeleteView):
    model = models.TestType
    template_name = 'test_confirm_delete.html'
    success_url = reverse_lazy('administration:test_type_list')

