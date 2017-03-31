import requests, json#, pprint
from urllib.parse import urljoin
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from api.models import Terminal
from eHall.models import Ticket
from .models import Event
from .forms import *
from .serializers import EventSerializer

# Set the active attribute to activate the appropriate navbar button
eventContext = {
    'active': 'event',
}

def dashboard(request):
    if request.user.is_authenticated():
        page = request.GET.get('page')
        events = getEventPage(request, page)

        context = {
            'events': events,
        }
        return render(request, 'dashboard.html', {**eventContext, **context})
    else:
        return redirect("/login")

def add(request):
    if request.method == 'GET':
        return getAddForm(request)
    elif request.method == 'POST':
        form = AddForm(request.POST or None)
        if form.is_valid():
            event = form.save()
            event.creator = request.user
            event.save()

            ticketList = []
            for i in range(event.nbTickets):
                ticket = Ticket(
                    event = event,
                    price = event.ticketPrice,
                )
                ticketList.append(ticket)

            Ticket.objects.bulk_create(ticketList)
        else:
            return HttpResponse(status=400)

        events = getEventPage(request, 1)

        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})

def edit(request, eventId):
    if request.method == 'GET':
        return getEditForm(request, eventId)
    elif request.method == 'POST':
        event = Event.objects.get(pk=eventId)
        form = EditForm(request.POST or None, instance=event)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(status=400)

        events = getEventPage(request, 1)

        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})

def publish(request, eventId):
    if request.method == 'GET':
        return getPublishForm(request, eventId)
    elif request.method == 'POST':
        event = Event.objects.get(pk=eventId)
        form = PublishForm(request.POST or None, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            
            retailer = event.retailer
            auditorium = event.auditorium
            headers = {
                    'Content-Type': 'application/json',
                    'Authorization': retailer.key,
                }
            
            if retailer.pk == 1:
                return HttpResponse(status=501) # Not yet implemented
            elif retailer.pk == 2:
                # Add or edit the auditorium
                path = 'api/theater/'
                url = urljoin(retailer.url, path)
                response = requests.get(urljoin(url, str(event.auditorium_id)), headers=headers, timeout=10)
                
                auditoriumData = {
                        'theaterId': auditorium.pk,
                        'adminId': event.creator_id,
                        'name': auditorium.name,
                        'address': auditorium.address,
                        'city': auditorium.city,
                        'province': auditorium.province,
                        'postalCode': auditorium.postalCode,
                        'capacity': auditorium.capacity,
                        'image': auditorium.image,
                    }
                
                if response.status_code == 404:
                    # Create the auditorium on the remote site
                    response = requests.post(url, headers=headers, data=json.dumps(auditoriumData), timeout=10)
                else:
                    auditoriumData.pop('theaterId') # Do not send the auditorium ID when modifying
                    response = requests.put(urljoin(url, str(event.auditorium_id)), headers=headers, data=json.dumps(auditoriumData), timeout=10)
                
                # If the response is unsuccessful (HTTP response code not 2xx), return error 500.
                #pprint.pprint(response.text)
                response.raise_for_status()
                if str(response.status_code)[0] != '2':
                    return HttpResponse(status=500)
                    
                # Add the event
                path = 'api/show'
                url = urljoin(retailer.url, path)
                response = requests.get(urljoin(url, str(event.pk)), headers=headers, timeout=10)
                
                eventData = {
                    'showId': event.pk,
                    'theaterId': auditorium.pk,
                    'sticker': event.image,
                    'image': event.image,
                    'title': event.name,
                    'artist': event.artist,
                    'datetime': event.startDate.isoformat(),
                    'description': event.description,
                    'price': float(event.ticketPrice),
                    'isFeatured': False,
                    'isPublished': False,
                    'isOnSale': False,
                }
                
                if response.status_code == 404:
                    # Create the event on the remote site
                    response = requests.post(url, headers=headers, data=json.dumps(eventData), timeout=10)
                else:
                    eventData.pop('showId') # Do not send the event ID when modifying
                    response = requests.put(urljoin(url, str(event.auditorium_id)), headers=headers, data=json.dumps(eventData), timeout=10)
                    
                # If the response is unsuccessful (HTTP response code not 2xx), return error 500.
                #pprint.pprint(response.text)
                response.raise_for_status()
                if str(response.status_code)[0] != '2':
                    return HttpResponse(status=500)
                    
            # Operations were successful. Change the local model to reflect changes.
            event.isPublished = True
            event.save()
        else:
            return HttpResponse(status=400)

        events = getEventPage(request, 1)

        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})
        
def open(request, eventId):
    if request.method == 'GET':
        return getOpenForm(request, eventId)
    elif request.method == 'POST':
        event = Event.objects.get(pk=eventId)
        
        # API calls to retailer...
        
        event.isOnSale = True
        event.status = 'o'
        event.save()

        events = getEventPage(request, 1)

        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})

def close(request, eventId):
    if request.method == 'GET':
        return getCloseForm(request, eventId)
    elif request.method == 'POST':
        event = Event.objects.get(pk=eventId)
        event.status = 'c'
        
        # API calls to retailer...
        
        event.save()

        events = getEventPage(request, 1)

        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})

def delete(request, eventId):
    if request.method == 'GET':
        return getDeleteForm(request, eventId)
    elif request.method == 'POST':
        event = Event.objects.get(pk=eventId)
        event.delete()

        events = getEventPage(request, 1)

        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})

def statistics(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    tickets = Ticket.objects.filter(event=event)
    ticketsSold = tickets.filter(isSold=True)
    ticketsUsed = ticketsSold.filter(scannedBy__isnull=False)

    numTickets = tickets.count()
    numTicketsSold = ticketsSold.count()
    numTicketsUsed = ticketsUsed.count()

    terminalsUsed = ticketsUsed.values_list('scannedBy', flat=True).distinct()

    terminals = {}
    for terminal in terminalsUsed:
        terminals[terminal] = event.getNbTicketsScanned(terminal)

    context = {
        'event': event,
        'tickets': numTickets,
        'ticketsSold': numTicketsSold,
        'ticketsUsed': numTicketsUsed,
        'terminals': terminals,
    }
    return render(request, 'statisticsView.html', {**eventContext, **context})

def getPublishForm(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    form = PublishForm(instance=event)

    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'publishForm.html', {**eventContext, **context})

def getAddForm(request):
    form = AddForm()

    context = {
        'form': form,
    }
    return render(request, 'addForm.html', {**eventContext, **context})

def getEditForm(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    form = EditForm(instance=event)

    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'editForm.html', {**eventContext, **context})

def getPublishForm(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    form = PublishForm(instance=event)

    context = {
        'event': event,
        'form': form,
    }
    return render(request, 'publishForm.html', {**eventContext, **context})
    
def getOpenForm(request, eventId):
    event = get_object_or_404(Event, pk=eventId)

    context = {
        'event': event,
    }
    return render(request, 'openForm.html', {**eventContext, **context})

def getCloseForm(request, eventId):
    event = get_object_or_404(Event, pk=eventId)

    context = {
        'event': event,
    }
    return render(request, 'closeForm.html', {**eventContext, **context})

def getDeleteForm(request, eventId):
    event = get_object_or_404(Event, pk=eventId)

    context = {
        'event': event,
    }
    return render(request, 'deleteForm.html', {**eventContext, **context})

def getEventPage(request, page):
    user = request.user
    events = Event.objects.all().order_by('-id') if request.user.is_superuser else Event.objects.filter(creator=user.id).order_by('-id')
    paginator = Paginator(events, 10) # Show 10 events per page

    try:
        # Display the requested page
        events = paginator.page(page)
    except PageNotAnInteger:
        # Display the first page if no valid page argument is provided
        events = paginator.page(1)
    except EmptyPage:
        # Display the last page if the requested range exceeds the number of entries
        events = paginator.page(paginator.num_pages)

    return events
