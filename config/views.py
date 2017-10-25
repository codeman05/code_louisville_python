from django.views.generic import ListView

from testrequests import models


class SiteHomepageListView(ListView):
    model = models.Test
    template_name = 'site_homepage.html'
