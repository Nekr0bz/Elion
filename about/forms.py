# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from services.models import Service
from .models import AreasWork

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


class SubmitApplication(forms.Form):
    choice_region = [(None, 'Выберите город')] + AreasWork.objects.get_list_dates() + [('0', 'Другой')]
    choice_service = [(None, 'Выберите интересующую услугу')] + Service.objects.get_list_dates() + [('0', 'Другая')]

    first_name = forms.CharField(max_length=35, label='Выше Имя',
                                 widget=forms.TextInput(attrs={
                                    'placeholder': 'Ваше Имя',
                                    'class': 'form-control'}))
    last_name = forms.CharField(max_length=35, label='Ваша Фамилия',
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Ваша Фамилия',
                                    'class': 'form-control'}))
    phone = PhoneNumberField(label='Ваш Номер Телефона',
                             widget=PhoneNumberInternationalFallbackWidget(attrs={
                                    'placeholder': '+7 000 000 00 00',
                                    'class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email',
                             widget=forms.EmailInput(attrs={
                                    'placeholder': 'Ваш Email',
                                    'class': 'form-control email'}))
    service = forms.ChoiceField(label='Услуга', choices=choice_service,
                                widget=forms.Select(attrs={
                                    'class': 'form-control'}))
    region = forms.ChoiceField(label='Область', choices=choice_region,
                               widget=forms.Select(attrs={
                                   'class': 'form-control'}))
    address = forms.CharField(label='Полный адрес',
                              widget=forms.TextInput(attrs={
                                    'placeholder': 'Полный адрес (улица, дом, квартира)',
                                    'class': 'form-control'}))
    message = forms.CharField(label='Дополнительная информация (необязательно)',
                              required=False,
                              widget=forms.Textarea(attrs={
                                    'placeholder': 'Дополнительная информация о вашем заказе'}))
    error_css_class = 'error'

    def _generate_message(self):
        subject = 'Заявка от пользователя сайта'
        region = AreasWork.objects.get(id=self.cleaned_data['region'])
        service = Service.objects.get(id=self.cleaned_data['service'])

        message = 'Имя: ' + self.cleaned_data['first_name'].encode('utf-8') + '\n'
        message += 'Фамилия: ' + self.cleaned_data['last_name'].encode('utf-8') + '\n'
        message += 'Email: ' + self.cleaned_data['email'].encode('utf-8') + '\n'
        message += 'Телефон: ' + str(self.cleaned_data['phone']) + '\n'
        message += 'Тип услуги: ' + str(service) + '\n'
        message += 'Регион: ' + str(region) + '\n'
        message += 'Полный адресс: ' + self.cleaned_data['address'].encode('utf-8') + '\n'
        message += 'Дополнительная информация: ' + self.cleaned_data.get('message', '').encode('utf-8')
        return subject, message

    def send_email(self):
        (subject, message) = self._generate_message()
        send_mail(subject, message, settings.EMAIL_HOST_USER, ['nekr0b@yandex.ru'])
