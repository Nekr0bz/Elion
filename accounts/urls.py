from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login/$', views.LoginViews.as_view(), name='login'),
]


