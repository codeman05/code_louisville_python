from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from . import models


class TestListView(ListView):
    template_name = 'testrequests/test_list_view_template.html'
    model = models.Test


class TestDeleteView(DeleteView):
    model = models.Test
    template_name = 'testrequests/test_confirm_delete.html'
    success_url = reverse_lazy('tests:list')


class DepartmentCreateView(CreateView):
    model = models.Department
    template_name = 'testrequests/form_create_template.html'
    fields = (
        'name',
        'manager',
    )


class EmployeeCreateView(CreateView):
    model = models.Employee
    template_name = 'testrequests/form_create_template.html'
    fields = (
        'first_name',
        'last_name',
        'email',
        'phone',
        'department',
    )


class CustomerCreateView(CreateView):
    model = models.Customer
    template_name = 'testrequests/form_create_template.html'
    fields = (
        'first_name',
        'last_name',
        'company',
        'address',
        'email',
        'phone',
    )


class TestTypeCreateView(CreateView):
    model = models.TestType
    template_name = 'testrequests/form_create_template.html'
    fields = (
        'name',
        'code',
        'price',
        'department',
    )


class TestCreateView(CreateView):
    template_name = 'testrequests/form_create_template.html'
    model = models.Test
    fields = (
        'customer',
        'quote_number',
        'po_number',
        'test_type',
        'air_flow_rate',
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
    )


class TestUpdateView(UpdateView):
    template_name = 'testrequests/form_create_template.html'
    model = models.Test
    fields = (
        'customer',
        'quote_number',
        'po_number',
        'test_type',
        'air_flow_rate',
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
    )

