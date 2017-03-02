from django.contrib import admin

from models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['usr', 'title', 'datetime']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(News, NewsAdmin)


