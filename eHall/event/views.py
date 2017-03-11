# Create your views here.

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event

# Set the active attribute to activate the appropriate navbar button
eventContext = {
    'active': 'event',
}

def dashboard(request):
    events = Event.objects.all()
    paginator = Paginator(events, 10) # Show 10 events per page
    
    page = request.GET.get('page')
    try:
        # Display the requested page
        events = paginator.page(page)
    except PageNotAnInteger:
        # Display the first page if no valid page argument is provided
        events = paginator.page(1)
    except EmptyPage:
        # Display the last page if the requested range exceeds the number of entries
        events = paginator.page(paginator.num_pages)
        
    context = {
        'events': events,
    }  
    return render(request, 'dashboard.html', {**eventContext, **context})
    
def edit(request, eventId):
    event = Event.objects.get(pk=eventId)
    context = {
        'event': event,
    }
    return render(request, 'edit.html', {**eventContext, **context})
