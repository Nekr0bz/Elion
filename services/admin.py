# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer

from .models import Service, ServiceSections
from Elion.settings import THUMBNAIL_ALIASES as th_options


class SectionsInline(admin.StackedInline):
    model = ServiceSections
    extra = 0
    readonly_fields = ('thumb_img',)
    fields = ('type', 'title', 'content', ('thumb_img', 'img'))

    def thumb_img(self, obj):
        th = get_thumbnailer(obj.img)
        th = th.get_thumbnail(th_options["services.ServiceSections"]["section_adm"])
        ret = '<a href="'+str(obj.img.url)+'"><img src=/media/'+str(th)+'/></a>'
        return mark_safe(ret)
    thumb_img.short_description = 'Миниатюра изображения'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ('thumb_main_img',)
    fields = ('title', 'content', ('thumb_main_img', 'main_img'))
    inlines = [SectionsInline]

    # TODO: Упростить!
    def thumb_main_img(self, obj):
        th = get_thumbnailer(obj.main_img)
        th = th.get_thumbnail(th_options["services.Service"]["srvc_adm"])
        ret = '<a href="'+str(obj.main_img.url)+'"><img src=/media/'+str(th)+'/></a>'
        return mark_safe(ret)
    thumb_main_img.short_description = 'Миниатюра изображения для превью'


admin.site.register(Service, ServiceAdmin)