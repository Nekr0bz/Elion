from django.views.generic import ListView

from services.models import Service


class ServicesMainViews(ListView):
    model = Service
    template_name = 'services/list.html'

