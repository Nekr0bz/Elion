from django.conf.urls import url, include, static
from django.contrib import admin
from . import settings

from main import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls),
    url(r'^services/', include('services.urls', namespace='services')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^guestbook/', include('guestbook.urls', namespace='guestbook')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)