from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(TimeStamp):
    name = models.CharField(null=False, max_length=30, unique=True, verbose_name='department name', help_text='Example: Finance')
    manager = models.CharField(null=False, max_length=30, help_text='Example: Rick Pitino')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('administration:department_list')


class Employee(TimeStamp):
    department = models.ForeignKey(Department, help_text=mark_safe("If the department is not listed here, you must add it on the <a href='/administration/department/create'>Departments page.</a>"))
    first_name = models.CharField(null=False,max_length=30)
    last_name = models.CharField(null=False, max_length=30)
    email = models.EmailField(null=False, max_length=50, help_text='Example: rpitino@notUofL.com')
    phone = models.CharField(null=False, max_length=12, help_text='Example: 502-555-1234')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('administration:employee_list')


class Customer(TimeStamp):
    first_name = models.CharField(null=False, max_length=30)
    last_name = models.CharField(null=False, max_length=30)
    company = models.CharField(null=False, max_length=50)
    email = models.EmailField(null=False, max_length=50, help_text='Example: rpitino@notUofL.com')
    address = models.CharField(null=True, blank=True, max_length=200, help_text='Example: 1234 Main Street, Anywhere, KY, USA')
    phone = models.CharField(null=True, blank=True, max_length=20, help_text='Example: +1 555-555-5555')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('administration:customer_list')


class TestType(TimeStamp):
    name = models.CharField(null=False, max_length=50, verbose_name='name of test')
    code = models.CharField(null=True, blank=True, max_length=10, verbose_name='test short code', help_text='Example: RT-IE-DHC. Must be less than 10 characters.')
    price = models.DecimalField(null=True, blank=True, max_digits=7, decimal_places=2, help_text='Example: 5000.00')
    department = models.ForeignKey(Department, help_text=mark_safe("Must be assigned to a department. If the department is not listed here, you must add it on the <a href='/administration/department/create'>Departments page.</a>"))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('administration:test_type_list')


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
    initial_loading_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    hi_pulse_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    lo_pulse_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    pulse_ms_on = models.PositiveIntegerField(null=True, blank=True, help_text='in milliseconds')
    pulse_ms_off = models.PositiveIntegerField(null=True, blank=True, help_text='in milliseconds')
    pulse_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')
    not_to_exceed_pressure = models.PositiveIntegerField(null=True, blank=True, help_text='in W.G.')

    def get_absolute_url(self):
        return reverse('administration:test_request_list')