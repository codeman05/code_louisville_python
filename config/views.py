from django.views.generic import ListView, TemplateView
from django_tables2 import RequestConfig

from administration import models
from administration import tables


class DashboardListView(ListView):
    model = models.Test
    template_name = 'dashboard.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(DashboardListView, self).get_context_data(**kwargs)
        table = tables.TestRequestsTable(models.Test.objects.all())
        RequestConfig(self.request, paginate={'per_page': 30}).configure(table)
        context['table'] = table
        return context


class CustomizeSettingsTemplateView(TemplateView):
    template_name = 'customize_navbar.html'
