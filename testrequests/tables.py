import django_tables2 as tables
from django_tables2.utils import A

from . import models


class TestRequestsTable(tables.Table):
    """Defines the attributes necessary to create the Test Request Table
    used on the Orders Database Page. The desire was to have a link that could
    allow editing or deleting a record.  The id field was chosen for this task.
    """

    id = tables.LinkColumn('tests:update', args=[A('pk')])

    class Meta:
        model = models.Test
        fields = (
            'id',
            'customer',
            'quote_number',
            'po_number',
            'test_type',
            'air_flow_rate',
            'manufacturer',
            'barcode_number',
        )
        attrs = {'id': 'dataTable', 'class': 'table table-bordered', 'width': '100%', 'cellspacing': '0'}
        empty_text = 'There are no results matching the search criteria'

