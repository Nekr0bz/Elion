# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_delete, pre_save
from generic.signals import del_imgs__pre_delete, del_imgs__pre_save

import datetime


class AreasWork(models.Model):
    region = models.CharField(verbose_name='Регион', max_length=30)

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
    mission = models.TextField('Специализация компании')
    mission_img = models.ImageField(upload_to='about/', help_text='470x167px',
                                    verbose_name='Главная цель (миссия) компании')

    description_services = models.TextField('Общее описание услуг')
    who_we_are1 = models.TextField('"Кто мы?" - первый абзац')
    who_we_are2 = models.TextField('"Кто мы?" - второй абзац')
    value_company = models.TextField('Гордость компании')

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

    class Meta:
        verbose_name = 'Важно число компании'
        verbose_name_plural = 'Четыре важные цифры компании'

    def get_start_number(self):
        return 1 if self.number < 30 else 10


class Employees(models.Model):
    full_name = models.CharField('Полное имя', max_length=30)
    position = models.CharField('Должность', max_length=30)
    contact = models.CharField('Контактная информация', max_length=30, blank=True,
                               help_text='Email, телефон или персональный сайт')
    review = models.TextField('Отзыв сотрудника', max_length=255)
    avatar = models.ImageField(upload_to='employees/', help_text='130x130px', verbose_name='Фотография сотрудника')

    class Meta:
        db_table = 'Employees'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __unicode__(self):
        return self.full_name

    def get_images_fields(self):
        return self.avatar,


class ValuesCompany(models.Model):
    title_main = models.CharField('Главный заголовок', max_length=20)
    title_other = models.CharField('Второй заголовок', max_length=50)
    text = models.TextField('Описание')

    class Meta:
        verbose_name = 'Ценности компании'
        verbose_name_plural = 'Ценности компании'

    def __unicode__(self):
        return self.title_main

# Регистрация callback-функций сигналов
pre_delete.connect(del_imgs__pre_delete, sender=StaticDates)
pre_save.connect(del_imgs__pre_save, sender=StaticDates)
pre_delete.connect(del_imgs__pre_delete, sender=Employees)
pre_save.connect(del_imgs__pre_save, sender=Employees)