from django.db import models


class FilterTest(models.Model):
    customer = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    test_type = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )

    def __str__(self):
        return self.customer


class Filter(models.Model):
    test_number = models.ForeignKey(FilterTest)
    filter_model_number = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    barcode_number = models.CharField(
        blank=True,
        null=False,
        max_length=10
    )

