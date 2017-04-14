# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.contrib import messages
from django.contrib.auth import logout, login as auth_login
from django.contrib.auth.views import login as view_login
from django.shortcuts import redirect
from .forms import SignInForm, SignUpForm
from generic.mixins import NextPageMixin


class LoginView(NextPageMixin, FormView):
    form_class = SignInForm
    template_name = 'accounts/sign_in.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        view_login(self.request, authentication_form=SignInForm)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.values()[0][0])
        return super(LoginView, self).form_invalid(form)


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.META.get('HTTP_REFERER', '/')
        return url

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class RegisterView(NextPageMixin, FormView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm

    def form_valid(self, form):
        auth_login(self.request, form.save())
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.values()[0][0])
        return super(RegisterView, self).form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())

        return super(RegisterView, self).get(request, *args, **kwargs)





