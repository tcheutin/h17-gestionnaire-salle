# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Event
from .forms import *

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
        #'page_obj': paginator,
    }  
    return render(request, 'dashboard.html', {**eventContext, **context})
    
def add(request):
    form = AddForm()
    
    context = {
        'addForm': form,
    }
    return render(request, 'addForm.html', {**eventContext, **context})
    
def edit(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    form = EditForm()
    
    context = {
        'event': event,
        'editForm': form,
    }
    return render(request, 'editForm.html', {**eventContext, **context})
    
def delete(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    form = DeleteForm()
    
    context = {
        'event': event,
        'deleteForm': form,
    }
    return render(request, 'deleteForm.html', {**eventContext, **context})
    
def statistics(request, eventId):
    event = get_object_or_404(Event, pk=eventId)
    
    context = {
        'event': event,
    }
    return render(request, 'statisticsView.html', {**eventContext, **context})
