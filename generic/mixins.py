from django.views.generic.base import ContextMixin


class NextPageMixin(ContextMixin):
    def get_success_url(self):
        try:
            url = self.request.GET['next']
        except KeyError:
            url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get_context_data(self, **kwargs):
        context = super(NextPageMixin, self).get_context_data(**kwargs)
        context["next"] = self.get_success_url()
        return context