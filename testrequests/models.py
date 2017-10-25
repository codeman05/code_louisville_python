from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings

from . import qr_code


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(TimeStamp):
    name = models.CharField(max_length=30, unique=True)
    manager = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Employee(TimeStamp):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12, help_text='XXX-XXX-XXXX')
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Customer(TimeStamp):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class TestType(TimeStamp):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=7, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.name


class Filter(models.Model):
    manufacturer = models.CharField(max_length=30)
    model_number = models.CharField(max_length=30)
    part_number = models.CharField(max_length=30, blank=True, null=True)
    filter_type = models.CharField(max_length=30, blank=True, null=True)
    date_code = models.CharField(max_length=30, blank=True, null=True)
    nominal_height = models.PositiveIntegerField(blank=True, null=True, help_text='inches')
    nominal_width = models.PositiveIntegerField(blank=True, null=True, help_text='inches')
    nominal_depth = models.PositiveIntegerField(blank=True, null=True, help_text='inches')
    pleat_quantity = models.PositiveIntegerField(blank=True, null=True)
    pocket_quantity = models.PositiveIntegerField(blank=True, null=True)
    media_type = models.CharField(max_length=30, blank=True, null=True)
    adhesive_type = models.CharField(max_length=30, blank=True, null=True)
    adhesive_amount = models.CharField(max_length=30, blank=True, null=True)
    disposal = models.BooleanField(default=False)
    #barcode_number = models.CharField(default=qr_code.get_barcode, max_length=10, blank=True, null=True)

    #location = '/static/barcodes/{}.png'.format(barcode_number)
    #barcode_image = models.ImageField(default=location, blank=True, null=True)
    #barcode_url = models.URLField(default=location, blank=True, null=True)

    class Meta:
        abstract = True


class Test(TimeStamp, Filter):
    customer = models.ForeignKey(Customer)
    quote_number = models.CharField(max_length=30, blank=True, null=True)
    po_number = models.CharField(max_length=30, blank=True, null=True)

    test_type = models.ForeignKey(TestType)
    air_flow_rate = models.PositiveIntegerField()
    ISO_FINE = 'IF'
    ISO_COARSE = 'IC'
    ASHRAE = 'A'
    TEST_DUST_CHOICES = (
        (ISO_FINE, 'ISO Fine'),
        (ISO_COARSE, 'ISO Coarse'),
        (ASHRAE, 'ASHRAE'),
    )
    test_dust = models.CharField(max_length=2, choices=TEST_DUST_CHOICES, null=True, blank=True)
    final_resistance = models.PositiveIntegerField(blank=True, null=True, help_text='in W.G.')
    dust_feed_rate = models.PositiveIntegerField(blank=True, null=True, help_text='(gms / MCF)')
    initial_loading_pressure = models.PositiveIntegerField(blank=True, null=True, help_text='in W.G.')
    hi_pulse_pressure = models.PositiveIntegerField(blank=True, null=True, help_text='in W.G.')
    lo_pulse_pressure = models.PositiveIntegerField(blank=True, null=True, help_text='in W.G.')
    pulse_ms_on = models.PositiveIntegerField(blank=True, null=True, help_text='in milliseconds')
    pulse_ms_off = models.PositiveIntegerField(blank=True, null=True, help_text='in milliseconds')
    pulse_pressure = models.PositiveIntegerField(blank=True, null=True, help_text='in W.G.')
    not_to_exceed_pressure = models.PositiveIntegerField(blank=True, null=True, help_text='in W.G.')

    def __str__(self):
        if len(str(self.pk)) == 1:
            return "17-000{}".format(self.pk)
        if len(str(self.pk)) == 2:
            return "17-00{}".format(self.pk)
        if len(str(self.pk)) == 3:
            return "17-0{}".format(self.pk)
        if len(str(self.pk)) == 1:
            return "17-{}".format(self.pk)

    def get_absolute_url(self):
        return reverse('tests:list')








