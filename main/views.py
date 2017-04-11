from django.views.generic.base import TemplateView
from services.models import FourServiceDirection
from about.models import Employees, StaticDates, ValuesCompany
from news.models import News


class MainPageView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['static_dates'] = StaticDates.objects.all().last()
        context['employees'] = Employees.objects.all()
        context['news'] = News.objects.all()[:4]
        context['services'] = FourServiceDirection.objects.all()[:4]
        context['values_company'] = ValuesCompany.objects.all()
        return context