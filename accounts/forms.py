# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = auth_forms.ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        ),
    )

    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions')
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]


class SignInForm(auth_forms.AuthenticationForm):
    username = auth_forms.UsernameField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autofocus': '',
            'placeholder': 'Ваш Email',
            'class': 'form-control email'
        }),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Ваш Пароль',
            'class': 'form-control'
        }),
    )


class SignUpForm(UserCreationForm):
    email = auth_forms.UsernameField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autofocus': '',
            'placeholder': 'Введите Email',
            'class': 'form-control email'
        }),
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите Имя',
            'class': 'form-control'
        }),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите Фамлию',
            'class': 'form-control'
        }),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Введите Пароль',
            'class': 'form-control'
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторите Пароль',
            'class': 'form-control'
        }),
    )

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")
