from django.conf.urls import url, include, static
from django.contrib import admin
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^services/', include('services.urls', namespace='services')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
]

urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)