from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.auditorium, name='auditorium'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<auditoriumId>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<auditoriumId>[0-9]+)/delete/$', views.delete, name='delete'),
]
