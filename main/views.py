from django.views.generic.base import TemplateView


class MainPageView(TemplateView):
    template_name = "main/index.html"