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
    datetime = models.DateTimeField('Опубликована', default=timezone.now(), db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Новости'
        ordering = ['-datetime']


@receiver(pre_save, sender=News)
def slug_correction_pre_save_news(sender, instance, **kwargs):
    # TODO: News -> sender
    qs = News.objects.filter(slug=instance.slug)
    if qs.exists():
        count = qs.count()
        n = len(str(count-1))  # разрядность
        instance.slug = instance.slug[:-n] + count if count > 1 else instance.slug + '-'+count
