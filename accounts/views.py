from django.shortcuts import render
from django.contrib.admin.forms import AdminAuthenticationForm
from django.views.generic.edit import FormView


class LoginViews(FormView):
    form_class = AdminAuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        try:
            url = self.request.GET['next']
        except KeyError:
            url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get_context_data(self, **kwargs):
        context = super(LoginViews, self).get_context_data(**kwargs)
        context["next"] = self.get_success_url()
        return context






