# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField

from accounts.models import User


class News(models.Model):
    usr = models.ForeignKey(User)
    title = models.CharField('Заголовок', max_length=80, unique_for_date='datetime')
    description = models.TextField('Краткое описание', max_length=200)
    content = RichTextField(verbose_name='Основной контент')
    datetime = models.DateTimeField('Опубликована', db_index=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'News'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-datetime']

