import django_tables2 as tables

from . import models


class TestRequestsTable(tables.Table):
    class Meta:
        model = models.Test
        attrs = {'class': 'paleblue'}
        fields = (
            'id',
            'created',
            'modified',
            'cutomer',
            'manufacturer',
        )


