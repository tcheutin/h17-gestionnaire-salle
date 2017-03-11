# Create your views here.

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Auditorium

# Set the active attribute to activate the appropriate navbar button
auditoriumContext = {
    'active': 'auditorium',
}

def auditorium(request):
    auditoriums = Auditorium.objects.all()
    paginator = Paginator(auditoriums, 10) # Show 10 events per page
    
    page = request.GET.get('page')
    try:
        # Display the requested page
        auditoriums = paginator.page(page)
    except PageNotAnInteger:
        # Display the first page if no valid page argument is provided
        auditoriums = paginator.page(1)
    except EmptyPage:
        # Display the last page if the requested range exceeds the number of entries
        auditoriums = paginator.page(paginator.num_pages)
        
    context = {
        'auditoriums': auditoriums,
    }  
    return render(request, 'auditorium.html', {**auditoriumContext, **context})
    
def edit(request, auditoriumId):
    auditorium = Auditorium.objects.get(pk=auditoriumId)
    context = {
        'auditorium': auditorium,
    }
    return render(request, 'edit.html', {**eventContext, **context})
    