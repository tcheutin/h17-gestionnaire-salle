from django.conf.urls import url, include
# from rest_framework import routers
from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/terminals/$', views.TerminalList.as_view()),
    url(r'^api/tickets/$', views.TicketList.as_view()),
    url(r'^api/report/$', views.Report.as_view()),
    url(r'^api/close/$', views.Close.as_view()),
]
