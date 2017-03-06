# Create your views here.

from django.shortcuts import render

def auditorium(request):
    return render(request, 'auditorium.html')
