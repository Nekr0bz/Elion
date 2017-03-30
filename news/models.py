# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_delete, pre_save
from ckeditor_uploader.fields import RichTextUploadingField
from generic.shortcuts import dir_slug_path as SLUG_PATH
from generic.signals import del_imgs__pre_delete, del_imgs__pre_save


class News(models.Model):
    title = models.CharField('Заголовок', max_length=80, unique_for_date='datetime')
    description = models.TextField('Краткое описание', max_length=200)
    img = models.ImageField(upload_to=SLUG_PATH, verbose_name='Путь к изображению', help_text='750x308px')
    content = RichTextUploadingField(verbose_name='Основной контент')
    datetime = models.DateTimeField('Опубликована', db_index=True)
    slug = models.SlugField(unique=True)

    DIR_PATH_PREFIX = 'news/'

    class Meta:
        db_table = 'News'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-datetime']

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})

    def get_images_fields(self):
        return self.img,

    def __unicode__(self):
        return self.title


# Регистрация callback-функций сигналов
pre_delete.connect(del_imgs__pre_delete, sender=News)
pre_save.connect(del_imgs__pre_save, sender=News)