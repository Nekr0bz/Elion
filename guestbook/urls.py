from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.GuestBookIndexView.as_view(), name="index"),
    url(r'^delete/(?P<guestbook_id>[0-9]+)/$', views.GuestBookDeleteView.as_view(), name="delete"),
]