# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from ckeditor_uploader.fields import RichTextUploadingField
from generic.signals import del_imgs__pre_delete, del_imgs__pre_save


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    main_img = models.ImageField(upload_to='services/', verbose_name='Основное изображение', help_text='730х305px')
    content = RichTextUploadingField(verbose_name='Основное описание')

    DIR_PATH_PREFIX = 'services/'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        db_table = 'Service'

    def get_images_fields(self):
        return self.main_img,

    def __unicode__(self):
        return self.title

# Регистрация callback-функций сигналов
pre_delete.connect(del_imgs__pre_delete, sender=Service)
pre_save.connect(del_imgs__pre_save, sender=Service)




