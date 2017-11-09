from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django_tables2 import RequestConfig

from . import models
from . import tables
from . import mixins


########################################################################
#                                                                      #
# Create Views                                                         #
#                                                                      #
########################################################################


class CreateEmployeeView(LoginRequiredMixin, mixins.PageTitleMixin, CreateView):
    model = models.Employee
    page_title = "Employee"
    template_name = 'administration/create_update_template.html'
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'department',
    )


class CreateDepartmentView(LoginRequiredMixin, mixins.PageTitleMixin, CreateView):
    model = models.Department
    page_title = "Department"
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'manager',
    )


class CreateCustomerView(LoginRequiredMixin, mixins.PageTitleMixin, CreateView):
    model = models.Customer
    page_title = "Customer"
    template_name = 'administration/create_update_template.html'
    fields = (
        'company',
        'first_name',
        'last_name',
        'email',
        'address',
        'phone',
    )


class CreateTestTypeView(LoginRequiredMixin, mixins.PageTitleMixin, CreateView):
    model = models.TestType
    page_title = "Test Type"
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'code',
        'price',
        'department',
    )


class TestCreateView(CreateView):
    model = models.Test
    template_name = 'administration/requests_create_update_template.html'
    fields = (
        'customer',
        'test_type',
        'air_flow_rate',
        'quote_number',
        'po_number',
        'manufacturer',
        'model_number',
        'part_number',
        'filter_type',
        'date_code',
        'nominal_height',
        'nominal_width',
        'nominal_depth',
        'pleat_quantity',
        'pocket_quantity',
        'media_type',
        'adhesive_type',
        'adhesive_amount',
        'disposal',
        'test_dust',
        'final_resistance',
        'dust_feed_rate',
        'initial_loading_pressure',
        'hi_pulse_pressure',
        'lo_pulse_pressure',
        'pulse_ms_on',
        'pulse_ms_off',
        'pulse_pressure',
        'not_to_exceed_pressure',
        'location',
    )

    def get_context_data(self, **kwargs):
        context = super(TestCreateView, self).get_context_data(**kwargs)
        model_name = models.Test.__name__
        context['model_name'] = model_name
        return context


########################################################################
#                                                                      #
# List (Read) Views                                                    #
#                                                                      #
########################################################################


class EmployeeListView(mixins.PageTitleMixin, ListView):
    model = models.Employee
    page_title = "Employees"
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = tables.EmployeeTable(models.Employee.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class DepartmentListView(mixins.PageTitleMixin, ListView):
    model = models.Department
    page_title = "Departments"
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = tables.DepartmentTable(models.Department.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class CustomerListView(mixins.PageTitleMixin, ListView):
    model = models.Customer
    page_title = "Customers"
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = tables.CustomerTable(models.Customer.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class TestTypeListView(mixins.PageTitleMixin, ListView):
    model = models.TestType
    page_title = "Test Types"
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = tables.TestTypeTable(models.TestType.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class TestListView(ListView):
    model = models.Test
    template_name = 'administration/requests_list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super(TestListView, self).get_context_data(**kwargs)
        table = tables.TestRequestsTable(models.Test.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


########################################################################
#                                                                      #
# Update Views                                                         #
#                                                                      #
########################################################################


class EmployeeUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, UpdateView):
    model = models.Employee
    page_title = "Employee"
    template_name = 'administration/create_update_template.html'
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'department',
    )


class DepartmentUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, UpdateView):
    model = models.Department
    page_title = "Department"
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'manager',
    )


class CustomerUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, UpdateView):
    model = models.Customer
    page_title = "Customer"
    template_name = 'administration/create_update_template.html'
    fields = (
        'company',
        'first_name',
        'last_name',
        'email',
        'address',
        'phone',
    )


class TestTypeUpdateView(LoginRequiredMixin, mixins.PageTitleMixin, UpdateView):
    model = models.TestType
    page_title = "Test Type"
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'code',
        'price',
        'department',
    )


class TestUpdateView(UpdateView):
    model = models.Test
    template_name = 'administration/requests_create_update_template.html'
    fields = (
        'customer',
        'test_type',
        'air_flow_rate',
        'quote_number',
        'po_number',
        'manufacturer',
        'model_number',
        'part_number',
        'filter_type',
        'date_code',
        'nominal_height',
        'nominal_width',
        'nominal_depth',
        'pleat_quantity',
        'pocket_quantity',
        'media_type',
        'adhesive_type',
        'adhesive_amount',
        'disposal',
        'test_dust',
        'final_resistance',
        'dust_feed_rate',
        'initial_loading_pressure',
        'hi_pulse_pressure',
        'lo_pulse_pressure',
        'pulse_ms_on',
        'pulse_ms_off',
        'pulse_pressure',
        'not_to_exceed_pressure',
        'location',
        'barcode_number',
    )

    def get_context_data(self, **kwargs):
        context = super(TestUpdateView, self).get_context_data(**kwargs)
        model_name = models.Test.__name__
        context['model_name'] = model_name
        return context


########################################################################
#                                                                      #
# Delete Views                                                         #
#                                                                      #
########################################################################


class DeleteEmployeeView(LoginRequiredMixin, mixins.PageTitleMixin, DeleteView):
    model = models.Employee
    page_title = "Employee"
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:employee_list')


class DeleteDepartmentView(LoginRequiredMixin, mixins.PageTitleMixin, DeleteView):
    model = models.Department
    page_title = "Department"
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:department_list')


class DeleteCustomerView(LoginRequiredMixin, mixins.PageTitleMixin, DeleteView):
    model = models.Customer
    page_title = "Customer"
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:customer_list')


class DeleteTestTypeView(LoginRequiredMixin, mixins.PageTitleMixin, DeleteView):
    model = models.TestType
    page_title = "Test Type"
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:test_type_list')


class TestDeleteView(DeleteView):
    model = models.Test
    template_name = 'administration/requests_confirm_delete_template.html'
    success_url = reverse_lazy('administration:test_request_list')

