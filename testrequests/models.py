from django.core.urlresolvers import reverse

from django.db import models
from administration.models import TimeStamp, Customer, TestType


class Filter(models.Model):
    manufacturer = models.CharField(null=False, blank=False, max_length=30)
    model_number = models.CharField(null=False, blank=False, max_length=30)
    part_number = models.CharField(null=True, blank=True, max_length=30)
    filter_type = models.CharField(null=True, blank=True, max_length=30)
    date_code = models.CharField(null=True, blank=True, max_length=30)
    nominal_height = models.PositiveIntegerField(null=True, blank=True, help_text='inches')
    nominal_width = models.PositiveIntegerField(null=True, blank=True, help_text='inches')
    nominal_depth = models.PositiveIntegerField(null=True, blank=True, help_text='inches')
    pleat_quantity = models.PositiveIntegerField(null=True, blank=True)
    pocket_quantity = models.PositiveIntegerField(null=True, blank=True)
    media_type = models.CharField(null=True, blank=True, max_length=30)
    adhesive_type = models.CharField(null=True, blank=True, max_length=30)
    adhesive_amount = models.CharField(null=True, blank=True, max_length=30)
    disposal = models.BooleanField(default=False)

    barcode_number = models.CharField(null=True, blank=True, max_length=10)
    barcode_url = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True


class Test(TimeStamp, Filter):
    customer = models.ForeignKey(Customer)
    test_type = models.ForeignKey(TestType)
    quote_number = models.CharField(null=True, blank=True, max_length=30)
    po_number = models.CharField(null=True, blank=True, max_length=30)
    air_flow_rate = models.PositiveIntegerField(null=False, blank=False)

    # Dust Holding Testing
    ISO_FINE = 'IF'
    ISO_COARSE = 'IC'
    ASHRAE = 'A'
    TEST_DUST_CHOICES = (
        (ISO_FINE, 'ISO Fine'),
        (ISO_COARSE, 'ISO Coarse'),
        (ASHRAE, 'ASHRAE'),
    )
    test_dust = models.CharField(null=True, blank=True, choices=TEST_DUST_CHOICES, max_length=2)
    final_resistance = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    dust_feed_rate = models.PositiveIntegerField(null=True, blank=True, help_text='(gms / MCF)')

    # Aramco Testing
    initial_loading_pressure = models.PositiveIntegerField(null=True, help_text='in W.G.')
    hi_pulse_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    lo_pulse_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    pulse_ms_on = models.PositiveIntegerField(null=True, blank=True, help_text='in milliseconds')
    pulse_ms_off = models.PositiveIntegerField(null=True, blank=True, help_text='in milliseconds')
    pulse_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    not_to_exceed_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')

    def get_absolute_url(self):
        return reverse('tests:list')








