# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from generic.mixins import NextPageMixin
from .forms import SignInForm, SignUpForm
from .models import UserProfile


class LoginView(NextPageMixin, FormView):
    form_class = SignInForm
    template_name = 'accounts/sign_in.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, authentication_form=SignInForm)
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


class RegisterView(FormView):
    template_name = 'accounts/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        user.userprofile.send_activate_email()
        success_msg = 'На ваш email отправлено письмо для активации аккаунта!'
        messages.add_message(self.request, messages.SUCCESS, success_msg)
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, form.errors.values()[0][0])
        return super(RegisterView, self).form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(self.request.META.get('HTTP_REFERER', '/'))

        return super(RegisterView, self).get(request, *args, **kwargs)


class ConfirmView(RedirectView):
    url = reverse_lazy('accounts:login')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse_lazy('main'))

        user = get_object_or_404(UserProfile, activation_key=kwargs['activation_key']).user
        if user.userprofile.key_expires > timezone.now():
            user.is_active = True
            user.save()
            success_msg = 'Вы успешно зарегистрировались! Для того чтобы зайти на сайт, заполните форму ниже.'
            messages.add_message(self.request, messages.SUCCESS, success_msg)

        return super(ConfirmView, self).get(request, *args, **kwargs)








