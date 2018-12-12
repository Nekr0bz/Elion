# -*- coding: utf-8 -*-
from django.contrib import admin

from django.utils.safestring import mark_safe
from easy_thumbnails.files import get_thumbnailer

from .models import News
from Elion.settings import THUMBNAIL_ALIASES as th_options


class NewsAdmin(admin.ModelAdmin):
    """
    Раздел данных о новостях
    """
    list_display = ['title', 'slug', 'datetime']
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('image_thumb',)
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['slug']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['content']}),
        (None, {'fields': ['datetime']}),
        ('Изображение', {'fields': [('image_thumb', 'img')]})
    ]

    def image_thumb(self, obj):
        th = get_thumbnailer(obj.img)
        th = th.get_thumbnail(th_options["for_admin_panel"])
        ret = '<a href="' + str(obj.img.url) + '"><img src=/media/' + str(th) + '></a>'
        return mark_safe(ret)

    image_thumb.short_description = 'Миниатюра изображения'


admin.site.register(News, NewsAdmin)
