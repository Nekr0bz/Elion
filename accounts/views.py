# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.contrib.auth import logout, login as auth_login
from .forms import SignInForm, SignUpForm
from django.contrib.auth.views import login as view_login


class LoginView(FormView):
    form_class = SignInForm
    template_name = 'accounts/sign_in.html'

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
        # TODO: if user.is_active
        view_login(self.request, authentication_form=SignInForm)
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(FormView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm

    # TODO: сделать mixin для {{ next }}
    # TODO: редирект если уже авторизован
    # TODO: вывод ошибок
    def get_success_url(self):
        try:
            url = self.request.GET['next']
        except KeyError:
            url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context["next"] = self.get_success_url()
        return context

    def form_valid(self, form):
        auth_login(self.request, form.save())
        return super(RegisterView, self).form_valid(form)
