# Create your views here.

from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')
