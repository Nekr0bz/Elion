from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NewsListViews.as_view(), name="list"),
    url(r'^(?P<slug>[-\w]+)/$', views.NewsDetailViews.as_view(), name="detail"),
]