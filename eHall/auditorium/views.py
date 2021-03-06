from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from datetime import datetime
from .models import Auditorium
from event.models import Event
from django.contrib import messages
from .forms import *

# Set the active attribute to activate the appropriate navbar button
auditoriumContext = {
    'active': 'auditorium',
}

def auditorium(request):
    if request.user.is_authenticated():
        page = request.GET.get('page')
        auditoriums = getAuditoriumPage(request, page)

        context = {
            'auditoriums': auditoriums,
        }
        return render(request, 'auditorium.html', {**auditoriumContext, **context})
    else:
        return redirect("/login")

def add(request):
    if request.method == 'GET':
        return getAddForm(request)
    elif request.method == 'POST':
        form = AddForm(request.POST or None)
        if form.is_valid():
            auditorium = form.save()
            auditorium.creator = request.user
            auditorium.save()
            messages.success(request, "Auditorium sucessfully added!")
        else:
            messages.error(request, "An error occured. Auditorium could not be added!")

        auditoriums = getAuditoriumPage(request, 1)

        context = {
            'auditoriums': auditoriums,
        }
        return render(request, 'auditorium.html', {**auditoriumContext, **context})

def edit(request, auditoriumId):
    if request.method == 'GET':
        return getEditForm(request, auditoriumId)
    elif request.method == 'POST':
        auditorium = Auditorium.objects.get(pk=auditoriumId)
        form = EditForm(request.POST or None, instance=auditorium)
        if form.is_valid():
            form.save()
            messages.success(request, "Auditorium edited!")
        else:
            messages.error(request, "An error occured. Auditorium could not be added!")

        auditoriums = getAuditoriumPage(request, 1)

        context = {
            'auditoriums': auditoriums,
        }
        return render(request, 'auditorium.html', {**auditoriumContext, **context})

def delete(request, auditoriumId):
    if request.method == 'GET':
        return getDeleteForm(request, auditoriumId)
    elif request.method == 'POST':
        auditorium = Auditorium.objects.get(pk=auditoriumId)
        auditorium.delete()
        messages.success(request, "Auditorium sucessfully deleted!")

        auditoriums = getAuditoriumPage(request, 1)

        context = {
            'auditoriums': auditoriums,
        }
        return render(request, 'auditorium.html', {**auditoriumContext, **context})

def events(request, auditoriumId):
    auditorium = get_object_or_404(Auditorium, pk=auditoriumId)
    upcomingEvents = Event.objects.filter(auditorium=auditorium, startDate__gt=datetime.now()).order_by('startDate')

    context = {
        'events': upcomingEvents,
    }
    return render(request, 'eventView.html', {**auditoriumContext, **context})

def getAddForm(request):
    form = AddForm()

    context = {
        'form': form,
    }
    return render(request, 'addForm.html', {**auditoriumContext, **context})

def getEditForm(request, auditoriumId):
    auditorium = get_object_or_404(Auditorium, pk=auditoriumId)
    form = EditForm(instance=auditorium)

    context = {
        'auditorium': auditorium,
        'form': form,
    }
    return render(request, 'editForm.html', {**auditoriumContext, **context})

def getDeleteForm(request, auditoriumId):
    auditorium = get_object_or_404(Auditorium, pk=auditoriumId)

    context = {
        'auditorium': auditorium,
    }
    return render(request, 'deleteForm.html', {**auditoriumContext, **context})

def getAuditoriumPage(request, page):
    user = request.user
    auditoriums = Auditorium.objects.all().order_by('-id') if request.user.is_superuser else Auditorium.objects.filter(creator=user.id).order_by('-id')
    paginator = Paginator(auditoriums, 10) # Show 10 auditoriums per page

    try:
        # Display the requested page
        auditoriums = paginator.page(page)
    except PageNotAnInteger:
        # Display the first page if no valid page argument is provided
        auditoriums = paginator.page(1)
    except EmptyPage:
        # Display the last page if the requested range exceeds the number of entries
        auditoriums = paginator.page(paginator.num_pages)

    return auditoriums
