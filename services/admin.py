# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Service
from easy_thumbnails.files import get_thumbnailer
from django.utils.safestring import mark_safe
from Elion.settings import THUMBNAIL_ALIASES as th_options

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'img']
    readonly_fields = ('image_thumb',)
    fieldsets = [
        (None,                  {'fields': ['title']}),
        (None,                  {'fields': ['content']}),
        ('Изображение',         {'fields': [('image_thumb', 'img')]})
    ]

    def image_thumb(self, obj):
        th = get_thumbnailer(obj.img)
        th = th.get_thumbnail(th_options["services.Service.img"]["srvc"])
        ret = '<a href="'+str(obj.img.url)+'"><img src=/media/'+str(th)+'/></a>'
        return mark_safe(ret)
    image_thumb.short_description = 'Миниатюра изображения'


admin.site.register(Service, ServiceAdmin)