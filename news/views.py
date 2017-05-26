# -*- coding: utf-8 -*-
from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView

from .models import News


class NewsListViews(ArchiveIndexView):
    """
    Представление отвечающее 
    за отображение списка новостей
    """
    model = News
    date_field = 'datetime'
    template_name = 'news/list.html'
    paginate_by = 6
    allow_empty = True


class NewsDetailViews(DetailView):
    """
    Представление отвечающее 
    за отображение конкретной новости
    """
    model = News
    template_name = 'news/detail.html'


