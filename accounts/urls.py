from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^confirm/(?P<activation_key>[-\w]+)/$', views.ConfirmView.as_view(), name='confirm'),
]


