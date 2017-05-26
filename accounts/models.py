# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from phonenumber_field.modelfields import PhoneNumberField
from Elion import settings
import hashlib, datetime, random


class UserManager(BaseUserManager):
    """
    Менеджер для управления моделью пользователей
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Создание пользователя
        :return: экземпляр модели пользователя
        """
        if not email:
            raise ValueError('Email должен быть указан')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """
        Установка параметров при создании обычного пользователя
        :return: экземпляр модели пользователя
        """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Установка параметров при создании администратора
        :return: экземпляр модели пользователя
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель пользователей
    """
    email = models.EmailField(
        _('email address'),
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        _('last name'),
        max_length=30,
        blank=True
    )
    phone_number = PhoneNumberField('Номер телефона', blank=True, null=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'Users'

    def get_full_name(self):
        """
        Получение полного имя пользователя
        :return: имя и фамилия пользователя
        """
        full_name = '%s %s' % (self.first_name, self.last_name) if self.first_name and self.last_name else self.email
        return full_name.strip()

    def get_short_name(self):
        """
        Получение сокращённого имени пользователя
        :return: имя пользователя
        """
        return self.first_name


class UserAuthDataManager(models.Manager):
    """
    Менеджер для управления моделью отвечающий за активацию аккаунтов
    """
    def create_profile(self, user):
        """
        Создание модели для активации аккаунта
        :param user: экземпляр модели пользователя
        :type user: User
        :return: экземпляр модели для активации аккаунта
        """
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        activation_key = hashlib.sha1(str(salt+user.email).encode('utf-8')).hexdigest()
        key_expires = timezone.now() + datetime.timedelta(2)
        return self.model(user=user, activation_key=activation_key, key_expires=key_expires).save()


class UserAuthData(models.Model):
    """
    Модель отвечающая за активацию аккаунтов
    """
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField()

    objects = UserAuthDataManager()

    class Meta:
        db_table = 'User_AuthData'
        verbose_name = 'Данные активации аккаунта'
        verbose_name_plural = 'Данные активации аккаунтов'

    def send_activate_email(self):
        """
        Отправка сообщения для активации аккаунта пользователю на email
        """
        user = self.user
        key = self.activation_key
        host = "127.0.0.1:8000" if settings.DEBUG else settings.ALLOWED_HOSTS[-1]
        url = "http://"+host+reverse('accounts:confirm', kwargs={'activation_key': key})
        subject = 'Подтверждение регистрации'
        message = "Здравствуйте " + user.get_full_name()
        message += ", спасибо за регистрацию на нашем сайте.<br>Для активации вашего аккаунта, "
        message += "перейдите по ссылке:<br> "+url
        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

    def __unicode__(self):
        """
        Строковое представление объекта
        :return: полное имя пользователя
        """
        return self.user.get_full_name()