from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
# from django.template import RequestContext
# from rest_framework.response import Response
# from rest_framework import status
from django.http import HttpResponse

from api.models import Terminal
from event.models import Event
from report.models import Report
# Create your views here.

# TODO : setEvent ->
# TODO : setEventStatus -> Default: waiting; ready; in progress; stop;
terminalContext = {
    'active': 'terminal',
}

def dashboard(request):
    if request.user.is_authenticated():
        page = request.GET.get('page')
        terminals = Terminal.objects.raw('SELECT * FROM api_terminal')
        events = Event.objects.raw('SELECT * FROM event_event')
        context = {
            'terminals': terminals,
            'events': events,
        }
        return render(request, 'terminal.html', {**terminalContext, **context})

    else:
        return redirect("/login")

def SetEvent(request):
    print("SetEvent")
    if request.user.is_authenticated():
        terminal = request.GET.get("terminal", None)
        event = request.GET.get("event", None)

        t = Terminal.objects.get(id=terminal)
        e = Event.objects.get(id=event)
        if (t is not None) & (e is not None):
            print("Terminal: " + t.address)
            print("Event: " + e.name)

            t.event = e
            t.save()
    else:
        return redirect("/login")

    return HttpResponse("200")


def SetLaunch(request):
    print("Set launch for ticket scanning or closing")
    if request.user.is_authenticated():
        id = request.GET.get("id", None)
        value = request.GET.get("bool", None)

        e = Terminal.objects.get(id=id).event
        if (e is not None) & (value is not None):
            e.isClose = True
            if value == "true":
                e.isClose = False

            e.save()
            return HttpResponse("200")
        return HttpResponse("404")
    else:
        return redirect("/login")

    return HttpResponse("400")

def Logs(request, terminalId):
    if request.user.is_authenticated():
        page = request.GET.get('page')

        terminal = Terminal.objects.get(id=terminalId)
        logs = Report.objects.filter(terminal=terminal)
        context = {
            'terminal': terminal,
            'logs': logs,
        }

        return render(request, 'logs.html', {**terminalContext, **context})

    else:
        return redirect("/login")
