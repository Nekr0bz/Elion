from django.views.generic import ListView

from services.models import Service


class ServicesListViews(ListView):
    model = Service
    template_name = 'services/list.html'
