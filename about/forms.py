# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail

from Elion import settings


class ContactMessageForm(forms.Form):
    name = forms.CharField(max_length=35, widget=forms.TextInput(attrs={
        'placeholder': 'Ваше Имя',
        'class': 'form-control name'
    }))
    # TODO: проверка правельности email
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Ваш Email',
        'class': 'form-control email'
    }))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'placeholder': 'Тема',
        'class': 'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Сообщение'
    }))
    error_css_class = 'error'

    def _generate_message(self):
        subject = self.cleaned_data['subject'].encode('utf-8')
        message = 'Имя: ' + self.cleaned_data['name'].encode('utf-8') + '\n'
        message += 'Email: ' + self.cleaned_data['email'].encode('utf-8') + '\n'
        message += self.cleaned_data['message'].encode('utf-8')
        return subject, message

    def send_email(self):
        (subject, message) = self._generate_message()
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['nekr0b@yandex.ru'])
