from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^(?P<eventId>[0-9]+)/edit/$', views.edit, name='edit'),
]
