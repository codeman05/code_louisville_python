from django.views.generic import TemplateView


class SiteHomepageView(TemplateView):
    template_name = 'site_homepage.html'
