# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from generic.signals import del_imgs__pre_delete, del_imgs__pre_save

import datetime


class AreasWorkManager(models.Manager):
    def get_list_dates(self):
        return [(obj.id, obj.region) for obj in self.all()]


class AreasWork(models.Model):
    region = models.CharField(verbose_name='Регион', max_length=30)

    objects = AreasWorkManager()

    class Meta:
        db_table = 'AreasWork'
        verbose_name = 'Регион обслуживания'
        verbose_name_plural = 'Регионы обслуживания'

    def __unicode__(self):
        return self.region


class StaticDates(models.Model):
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    year_company_opening = models.IntegerField('Год открытия фирмы', choices=YEAR_CHOICES,
                                               default=datetime.datetime.now().year)
    history = models.TextField('История компании')
    mission = models.TextField('Главная цель (миссия) компании')
    mission_img = models.ImageField(upload_to='about/', help_text='470x167px',
                                    verbose_name='Главная цель (миссия) компании')

    description_services = models.TextField('Общее описание услуг')
    who_we_are1 = models.TextField('"Кто мы?" - первый абзац')
    who_we_are2 = models.TextField('"Кто мы?" - второй абзац')
    value_company = models.TextField('Ценности компании')

    class Meta:
        db_table = 'StaticDates'
        verbose_name = 'Статические данные'
        verbose_name_plural = 'Статические данные'

    def __unicode__(self):
        return 'Статические данные сайта'

    def get_images_fields(self):
        return self.mission_img,


class FourValuesCompany(models.Model):
    parent_static_dates = models.ForeignKey(StaticDates)
    number = models.IntegerField('Число')
    desc1 = models.CharField('Первая строка описания', max_length=20)
    desc2 = models.CharField('Вторая строка описания', max_length=20)


# Регистрация callback-функций сигналов
pre_delete.connect(del_imgs__pre_delete, sender=StaticDates)
pre_save.connect(del_imgs__pre_save, sender=StaticDates)