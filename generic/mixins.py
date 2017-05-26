# -*- coding: utf-8 -*-
from django.views.generic.base import ContextMixin


class NextPageMixin(ContextMixin):
    """
    Добавление в контекст шаблона данных
    о старнице на которую необходимо перейти
    """
    def get_success_url(self):
        """
        Возвращает страницу на которую необходимо перейти
        """
        try:
            url = self.request.GET['next']
        except KeyError:
            url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get_context_data(self, **kwargs):
        """
        Добавляет в контекст шаблона 
        url следующей страницы
        :return: контекст
        """
        context = super(NextPageMixin, self).get_context_data(**kwargs)
        context["next"] = self.get_success_url()
        return context