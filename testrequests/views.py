from django.views.generic import ListView, DetailView

from . import models


class TestListView(ListView):
    model = models.Test
    template_name = 'testrequests/test_list.html'


class TestDetailView(DetailView):
    model = models.Test
    # context_object_name = 'detail_list'
