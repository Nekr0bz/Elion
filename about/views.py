# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages

from .forms import ContactMessageForm
from Elion import settings


class ContactView(TemplateView):
    template_name = "about/contact.html"
    form = None

    def get(self, request, *args, **kwargs):
        self.form = ContactMessageForm()
        return super(ContactView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        self.form = ContactMessageForm(request.POST)
        if self.form.is_valid():
            (subject, message) = self.form.generate_message()
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['nekr0b@yandex.ru'])
            success_msg = 'Спасибо, что написали нам. Мы ответим вам в ближайщее время!'
            messages.add_message(request, messages.SUCCESS, success_msg)
            return redirect('contacts')
        else:
            messages.add_message(request, messages.ERROR, 'Ошибка! Сообщение не отправленно!')
            return super(ContactView, self).get(request, *args, **kwargs)

