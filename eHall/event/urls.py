from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^event$', views.dashboard, name='dashboard'),
]
