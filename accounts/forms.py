# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from Elion.settings import HIDE_PERMS_MODELS
from .models import User, UserAuthData


class UserCreationForm(forms.ModelForm):
    """
    Форма создания нового пользователя
    """
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
        """
        Проверка подтверждения пароля
        :return: Пароль
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        """
        Сохранение нового пользователя в БД
        :return: Экземпляр пользователя
        """
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    Форма обновления данных о пользователе
    """
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
        """
        Конструктор формы
        """
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions')
        if f is not None:
            all_perms = f.queryset.select_related('content_type')
            hide_perms = list(ContentType.objects.filter(model__in=HIDE_PERMS_MODELS))
            f.queryset = all_perms.exclude(content_type__in=hide_perms)

    def clean_password(self):
        return self.initial["password"]


class SignInForm(auth_forms.AuthenticationForm):
    """
    Форма авторизации
    """
    error_messages = {
        'invalid_login': "Пользователя с таким email и паролем не существует ",
        'inactive': "Простите, но администрторы сайта вас заблокировали"
    }

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
    """
    Форма регистрации
    """
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

    def save(self, commit=True):
        """
        Сохранение нового пользователя в БД
        :return: Экземпляр пользователя
        """
        user = super(SignUpForm, self).save(commit=False)
        user.is_active = False
        if commit:
            user.save()
            UserAuthData.objects.create_profile(user)
        return user
