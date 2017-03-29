# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from easy_thumbnails.files import get_thumbnailer
from ckeditor_uploader.fields import RichTextUploadingField

from accounts.models import User


class News(models.Model):
    title = models.CharField('Заголовок', max_length=80, unique_for_date='datetime')
    description = models.TextField('Краткое описание', max_length=200)
    img = models.ImageField(upload_to='news/', verbose_name='Путь к изображению', help_text='750x308px')
    content = RichTextUploadingField(verbose_name='Основной контент')
    datetime = models.DateTimeField('Опубликована', db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'News'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-datetime']

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title


@receiver(pre_delete, sender=News)
def del_img_pre_del_news(sender, instance, **kwargs):
    get_thumbnailer(instance.img).delete_thumbnails()
    instance.img.delete(save=False)


@receiver(pre_save, sender=News)
def del_img_pre_save_news(sender, instance, **kwargs):
    try:
        this_service = News.objects.get(id=instance.id)
        if this_service.img != instance.img:
            get_thumbnailer(this_service.img).delete_thumbnails()
            this_service.img.delete(save=False)

    except News.DoesNotExist:
        pass
