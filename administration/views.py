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

    def get_context_data(self, **kwargs):
        context = super(CreateEmployeeView, self).get_context_data(**kwargs)
        model_name = models.Employee.__name__
        context['model_name'] = model_name
        return context


class CreateDepartmentView(CreateView):
    model = models.Department
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'manager',
    )

    def get_context_data(self, **kwargs):
        context = super(CreateDepartmentView, self).get_context_data(**kwargs)
        model_name = models.Department.__name__
        context['model_name'] = model_name
        return context


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

    def get_context_data(self, **kwargs):
        context = super(CreateCustomerView, self).get_context_data(**kwargs)
        model_name = models.Customer.__name__
        context['model_name'] = model_name
        return context


class CreateTestTypeView(CreateView):
    model = models.TestType
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'code',
        'price',
        'department',
    )

    def get_context_data(self, **kwargs):
        context = super(CreateTestTypeView, self).get_context_data(**kwargs)
        model_name = 'Test Type'
        context['model_name'] = model_name
        return context


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


class EmployeeListView(ListView):
    model = models.Employee
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        model_name = models.Employee.__name__
        context['model_name'] = model_name
        table = tables.EmployeeTable(models.Employee.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class DepartmentListView(ListView):
    model = models.Department
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentListView, self).get_context_data(**kwargs)
        model_name = models.Department.__name__
        context['model_name'] = model_name
        table = tables.DepartmentTable(models.Department.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class CustomerListView(ListView):
    model = models.Customer
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super(CustomerListView, self).get_context_data(**kwargs)
        model_name = models.Customer.__name__
        context['model_name'] = model_name
        table = tables.CustomerTable(models.Customer.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class TestTypeListView(ListView):
    model = models.TestType
    template_name = 'administration/list_view_template.html'

    def get_context_data(self, **kwargs):
        context = super(TestTypeListView, self).get_context_data(**kwargs)
        context['model_name'] = 'Test Type'
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


class EmployeeUpdateView(UpdateView):
    model = models.Employee
    template_name = 'administration/create_update_template.html'
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'department',
    )

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        model_name = models.Employee.__name__
        context['model_name'] = model_name
        return context


class DepartmentUpdateView(UpdateView):
    model = models.Department
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'manager',
    )

    def get_context_data(self, **kwargs):
        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        model_name = models.Department.__name__
        context['model_name'] = model_name
        return context


class CustomerUpdateView(UpdateView):
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

    def get_context_data(self, **kwargs):
        context = super(CustomerUpdateView, self).get_context_data(**kwargs)
        model_name = models.Customer.__name__
        context['model_name'] = model_name
        return context


class TestTypeUpdateView(UpdateView):
    model = models.TestType
    template_name = 'administration/create_update_template.html'
    fields = (
        'name',
        'code',
        'price',
        'department',
    )

    def get_context_data(self, **kwargs):
        context = super(TestTypeUpdateView, self).get_context_data(**kwargs)
        model_name = 'Test Type'
        context['model_name'] = model_name
        return context


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


class DeleteEmployeeView(DeleteView):
    model = models.Employee
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        model_name = models.Employee.__name__
        context['model_name'] = model_name
        return context


class DeleteDepartmentView(DeleteView):
    model = models.Department
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:department_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        model_name = models.Department.__name__
        context['model_name'] = model_name
        return context


class DeleteCustomerView(DeleteView):
    model = models.Customer
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        model_name = models.Customer.__name__
        context['model_name'] = model_name
        return context


class DeleteTestTypeView(DeleteView):
    model = models.TestType
    template_name = 'administration/confirm_delete_template.html'
    success_url = reverse_lazy('administration:test_type_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        model_name = 'Test Type'
        context['model_name'] = model_name
        return context


class TestDeleteView(DeleteView):
    model = models.Test
    template_name = 'administration/requests_confirm_delete_template.html'
    success_url = reverse_lazy('administration:test_request_list')

