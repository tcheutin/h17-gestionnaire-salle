# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event, Ticket
from .forms import *

# Set the active attribute to activate the appropriate navbar button
eventContext = {
    'active': 'event',
}

def dashboard(request):
    page = request.GET.get('page')
    events = getEventPage(page)
        
    context = {
        'events': events,
    }
    return render(request, 'dashboard.html', {**eventContext, **context})
    
def add(request):
    if request.method == 'GET':
        return getAddForm(request)
    elif request.method == 'POST':
        form = AddForm(request.POST or None)
        if form.is_valid():
            event = form.save()
            ticketList = []
            for i in range(1, event.nbTickets):
                ticket = Ticket(
                    event = event,
                    price = event.ticketPrice,
                )
                ticketList.append(ticket)
                
            Ticket.objects.bulk_create(ticketList)
            
        events = getEventPage(1)
        
        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})
    
def edit(request, eventId):
    if request.method == 'GET':
        return getEditForm(request, eventId)
    elif request.method == 'POST':
        form = EditForm(request.POST or None)
        if form.is_valid():
            event = form.save(commit=False)
            event.id = eventId
            event.save()
            
        events = getEventPage(1)
        
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
        
        events = getEventPage(1)
        
        context = {
            'events': events,
        }
        return render(request, 'eventTable.html', {**eventContext, **context})
    
def statistics(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    tickets = Ticket.objects.filter(event=event)
    ticketsSold = tickets.filter(isSold=True)
    
    numTickets = tickets.count()
    numTicketsSold = ticketsSold.count()
    numTicketsUsed = ticketsSold.filter(isUsed=True).count()
    
    context = {
        'event': event,
        'tickets': numTickets,
        'ticketsSold': numTicketsSold,
        'ticketsUsed': numTicketsUsed,
    }
    return render(request, 'statisticsView.html', {**eventContext, **context})
    
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
    
def getDeleteForm(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    
    context = {
        'event': event,
    }
    return render(request, 'deleteForm.html', {**eventContext, **context})
    
def getEventPage(page):
    events = Event.objects.order_by('-id')
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
