from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^auditorium$', views.auditorium, name='auditorium'),
]
