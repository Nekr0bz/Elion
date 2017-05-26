# -*- coding: utf-8 -*-
from django.views.generic import ListView

from services.models import Service


class ServicesMainViews(ListView):
    """
    Представление отвечающее 
    за отображение услуг
    """
    model = Service
    template_name = 'services/list.html'

