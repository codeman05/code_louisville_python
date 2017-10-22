from django import forms

from . import models


class OrderForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'company',
            'name',
            'email'
        ]


class TestForm(forms.ModelForm):
    class Meta:
        model = models.Test
        fields = [
            'test_type',
            'air_flow_rate',
            'filter_description'
        ]
