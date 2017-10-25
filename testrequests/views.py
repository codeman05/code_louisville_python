from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from . import models


class TestListView(ListView):
    model = models.Test


class TestDeleteView(DeleteView):
    model = models.Test
    success_url = reverse_lazy('tests:list')


# class TestDetailView(DetailView):
#     model = models.Test


class TestCreateView(CreateView):
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
