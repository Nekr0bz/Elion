from django.conf.urls import url, include, static
from django.contrib import admin

from main import views as main_views
from about import views as about_views
from services import views as services_views

from . import settings



urlpatterns = [
    url(r'^$', main_views.MainPageView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls),
    url(r'^services/', services_views.ServicesMainViews.as_view(), name='services'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^contacts/$', about_views.ContactView.as_view(template_name='about/contact.html'), name='contacts'),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^guestbook/', include('guestbook.urls', namespace='guestbook')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)