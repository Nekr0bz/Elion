# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer
from Elion.settings import THUMBNAIL_ALIASES as th_options
from .models import  StaticDates, FourValuesCompany, AreasWork


class FourValuesCompanyInline(admin.StackedInline):
    model = FourValuesCompany
    extra = 0
    fields = ('number', ('desc1', 'desc2'))


class StaticDatesAdmin(admin.ModelAdmin):
    readonly_fields = ('thumb_mission_img',)
    inlines = [FourValuesCompanyInline]
    fieldsets = [
        ('Информация о компании',       {'fields': [('history', 'year_company_opening'),
                                                    ('mission', 'thumb_mission_img', 'mission_img')]}),
        ('Описание компании',           {'fields': [('who_we_are1', 'who_we_are2'),
                                                    ('description_services', 'value_company')]})
    ]

    def thumb_mission_img(self, obj):
        th = get_thumbnailer(obj.mission_img)
        th = th.get_thumbnail(th_options["about.StaticDates"]["about_adm"])
        ret = '<a href="'+str(obj.mission_img.url)+'"><img src=/media/'+str(th)+'/></a>'
        return mark_safe(ret)
    thumb_mission_img.short_description = 'Миниатюра изображения'


# Регистрация интерфейса для администратора в соответствии с моделями:
admin.site.register(StaticDates, StaticDatesAdmin)
admin.site.register(AreasWork)
