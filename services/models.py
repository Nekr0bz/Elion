# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from easy_thumbnails.files import get_thumbnailer


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    img = models.ImageField(upload_to='service/', verbose_name='Путь к изображению', help_text='150x150px')
    # TODO:Добавить лимиты

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        db_table = 'Service'


@receiver(pre_delete, sender=Service)
def del_img_pre_del_service(sender, instance, **kwargs):
    get_thumbnailer(instance.img).delete_thumbnails()
    instance.img.delete(save=False)

@receiver(pre_save, sender=Service)
def del_img_pre_save_service(sender, instance, **kwargs):
    try:
        this_service = Service.objects.get(id=instance.id)
        if this_service.img != instance.img:
            get_thumbnailer(this_service.img).delete_thumbnails()
            this_service.img.delete(save=False)

    except Service.DoesNotExist:
        pass
