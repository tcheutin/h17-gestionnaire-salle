from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^event/$', views.SetEvent, name='event'),
    url(r'^launch/$', views.SetLaunch, name='launch'),
    url(r'^logs/(?P<terminalId>[0-9]+$)', views.Logs, name='logs'),
]
