from django import forms

from . import models


class FilterTestForm(forms.ModelForm):
    class Meta:
        model = models.FilterTest
        fields = ['customer', 'test_type',]


class FilterForm(forms.ModelForm):
    class Meta:
        model = models.Filter
        fields = ['test_number', 'filter_model_number',]
        exclude = ['barcode_number',]
