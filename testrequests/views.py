from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from . import models
from . import qr_code


########################################################################
#                                                                      #
# Create Views                                                         #
#                                                                      #
########################################################################


class TestCreateView(CreateView):
    model = models.Test
    template_name = 'testrequests/form_create_template.html'
    context_object_name = 'object_list'
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


########################################################################
#                                                                      #
# List (Read) Views                                                    #
#                                                                      #
########################################################################


class TestListView(ListView):
    model = models.Test
    template_name = 'testrequests/test_list_view_template.html'
    context_object_name = 'object_list'


########################################################################
#                                                                      #
# Update Views                                                         #
#                                                                      #
########################################################################


class TestUpdateView(UpdateView):
    model = models.Test
    template_name = 'testrequests/form_create_template.html'
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


########################################################################
#                                                                      #
# Delete Views                                                         #
#                                                                      #
########################################################################


class TestDeleteView(DeleteView):
    model = models.Test
    template_name = 'testrequests/test_confirm_delete.html'
    success_url = reverse_lazy('tests:list')


