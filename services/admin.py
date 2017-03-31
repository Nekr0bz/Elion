# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer

from .models import Service
from Elion.settings import THUMBNAIL_ALIASES as th_options


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ('thumb_main_img',)
    fieldsets = [
        (None,                  {'fields': ['title']}),
        (None,                  {'fields': ['content']}),
        ('Изображения',         {'fields': [('thumb_main_img', 'main_img')]})
    ]

    # TODO: Упростить!
    def thumb_main_img(self, obj):
        th = get_thumbnailer(obj.main_img)
        th = th.get_thumbnail(th_options["services.Service"]["srvc_adm"])
        ret = '<a href="'+str(obj.main_img.url)+'"><img src=/media/'+str(th)+'/></a>'
        return mark_safe(ret)
    thumb_main_img.short_description = 'Миниатюра изображения для превью'


admin.site.register(Service, ServiceAdmin)