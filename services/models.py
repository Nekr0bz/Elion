# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from generic.signals import del_imgs__pre_delete, del_imgs__pre_save


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    main_img = models.ImageField(upload_to='services/', verbose_name='Основное изображение', help_text='730х305px')
    content = RichTextUploadingField(verbose_name='Основное описание')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        db_table = 'Service'

    def get_images_fields(self):
        return self.main_img,

    def __unicode__(self):
        return self.title


class ServiceSubsections(models.Model):
    SUB_SERVICE = (1, 'Дополнительная услуга')
    EXT_DESCRIPTION = (2, 'Дополнительное описание')
    TYPE_CHOICES = (SUB_SERVICE, EXT_DESCRIPTION)

    parent_service = models.ForeignKey(Service)
    title = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    content = RichTextField(verbose_name='Описание')
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name='Тип раздела', default=SUB_SERVICE)
    img = models.ImageField(upload_to='services/subsections/', verbose_name='Изображение',
                            help_text='Доп. услуга: 248х199px.\nДоп. описание: 151х161px.')

    class Meta:
        verbose_name = 'Дополнительный раздел'
        verbose_name_plural = 'Дополнительные разделы'
        db_table = 'Service_Subsections'
        ordering = ['type']

    def get_images_fields(self):
        return self.img,

    def __unicode__(self):
        return self.title


class FourServiceDirection(models.Model):
    title = models.CharField('Название', max_length=40)
    desc = models.TextField('Короткое описание', max_length=140)
    img = models.ImageField('Изображение', upload_to='services/directions/', help_text='154x142px')

    class Meta:
        verbose_name = 'Тематика услуг'
        verbose_name_plural = '4 направления услуг'
        db_table = 'FourServiceDirection'

    def get_images_fields(self):
        return self.img,

    def __unicode__(self):
        return self.title


# Регистрация callback-функций сигналов
# TODO: мб упростить?
pre_delete.connect(del_imgs__pre_delete, sender=Service)
pre_save.connect(del_imgs__pre_save, sender=Service)
pre_delete.connect(del_imgs__pre_delete, sender=ServiceSubsections)
pre_save.connect(del_imgs__pre_save, sender=ServiceSubsections)
pre_delete.connect(del_imgs__pre_delete, sender=FourServiceDirection)
pre_save.connect(del_imgs__pre_save, sender=FourServiceDirection)






