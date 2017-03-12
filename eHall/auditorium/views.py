# Create your views here.

from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Auditorium
from .forms import *

# Set the active attribute to activate the appropriate navbar button
auditoriumContext = {
    'active': 'auditorium',
}

def auditorium(request):
    if request.user.is_authenticated():
        auditoriums = Auditorium.objects.all()
        paginator = Paginator(auditoriums, 10) # Show 10 auditoriums per page

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
    else:
        return redirect("/login")

def add(request):
    if request.method == 'GET':
        return getAddForm(request)
    elif request.method == 'POST':
        form = AddForm(request.POST or None)
        if form.is_valid():
            auditorium = form.save()
            
        auditoriums = getAuditoriumPage(1)
        
        context = {
            'auditoriums': auditoriums,
        }
        return render(request, 'auditoriumTable.html', {**auditoriumContext, **context})
    
def edit(request, auditoriumId):
    if request.method == 'GET':
        return getEditForm(request, auditoriumId)
    elif request.method == 'POST':
        form = EditForm(request.POST or None)
        if form.is_valid():
            auditorium = form.save(commit=False)
            auditorium.id = auditoriumId
            auditorium.save()
            
        auditoriums = getAuditoriumPage(1)
        
        context = {
            'auditoriums': auditoriums,
        }
        return render(request, 'auditoriumTable.html', {**auditoriumContext, **context})
    
def delete(request, auditoriumId):
    if request.method == 'GET':
        return getDeleteForm(request, auditoriumId)
    elif request.method == 'POST':
        auditorium = Auditorium.objects.get(pk=auditoriumId)
        auditorium.delete()
        
        auditoriums = getAuditoriumPage(1)
        
        context = {
            'auditoriums': auditoriums,
        }
        return render(request, 'auditoriumTable.html', {**auditoriumContext, **context})
    
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
    
def getAuditoriumPage(page):
    auditoriums = Auditorium.objects.order_by('-id')
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
    