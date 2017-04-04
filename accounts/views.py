# -*- coding: utf-8 -*-
from django.contrib import messages
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.contrib.auth import logout
from .forms import AuthenticationForm
from django.contrib.auth.views import login


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        try:
            url = self.request.GET['next']
        except KeyError:
            url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context["next"] = self.get_success_url()
        return context

    def form_valid(self, form):
        login(self.request, authentication_form=AuthenticationForm)
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


