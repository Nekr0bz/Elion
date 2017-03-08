# -*- coding: utf-8 -*-
from django.db import models

from accounts.models import User


class GuestBook(models.Model):
    usr = models.ForeignKey(User, verbose_name='Пользователь')
    parent = models.ForeignKey('GuestBook', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(verbose_name='Содержание')
    datetime = models.DateTimeField('Опубликован', db_index=True, auto_now=True)

    class Meta:
        db_table = 'GuestBook'
        ordering = ['-datetime']
