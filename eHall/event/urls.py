from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<eventId>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<eventId>[0-9]+)/publish/$', views.publish, name='publish'),
	url(r'^(?P<eventId>[0-9]+)/close/$', views.close, name='close'),
    url(r'^(?P<eventId>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<eventId>[0-9]+)/statistics/$', views.statistics, name='statistics'),
]
