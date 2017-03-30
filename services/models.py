# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.files import get_thumbnailer

# TODO: вынести
def dir_slug_path(instance, filename):
    # Модель должна иметь поле 'slug' и 'DIR_PATH_PREFIX'
    return instance.DIR_PATH_PREFIX+instance.slug+'/'+filename


class Service(models.Model):
    DIR_PATH_PREFIX = 'services/'
    # tuple_images = (main_img, prev_img)

    # Fields:
    title = models.CharField(max_length=50, unique=True, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=100, verbose_name='Краткое описание')
    main_img = models.ImageField(upload_to=dir_slug_path, verbose_name='Основное изображение', help_text='730х305px')
    prev_img = models.ImageField(upload_to=dir_slug_path, verbose_name='Изображение для превью', help_text='354х204px')
    content = RichTextUploadingField(verbose_name='Основное описание')



    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        db_table = 'Service'

    def get_absolute_url(self):
        return reverse('services:detail', kwargs={'slug': self.slug})

    def __unicode__(self):
        return self.title


# TODO: вынести и упростить
@receiver(pre_delete, sender=Service)
def del_img_pre_del_service(sender, instance, **kwargs):
    # TODO: удалить директорию
    get_thumbnailer(instance.main_img).delete_thumbnails()
    instance.main_img.delete(save=False)
    get_thumbnailer(instance.prev_img).delete_thumbnails()
    instance.prev_img.delete(save=False)


@receiver(pre_save, sender=Service)
def del_img_pre_save_service(sender, instance, **kwargs):
    try:
        this_service = Service.objects.get(id=instance.id)
        if this_service.main_img != instance.main_img:
            get_thumbnailer(this_service.main_img).delete_thumbnails()
            this_service.main_img.delete(save=False)

        if this_service.prev_img != instance.prev_img:
            get_thumbnailer(this_service.prev_img).delete_thumbnails()
            this_service.prev_img.delete(save=False)

    except Service.DoesNotExist:
        pass