from django.views.generic.dates import ArchiveIndexView
from django.views.generic.detail import DetailView

from .models import News


class NewsListViews(ArchiveIndexView):
    model = News
    date_field = 'datetime'
    template_name = 'news/list.html'
    paginate_by = 6
    allow_empty = True


class NewsDetailViews(DetailView):
    model = News
    template_name = 'news/detail.html'


