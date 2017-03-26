from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Terminal
# Create your views here.

terminalContext = {
    'active': 'terminal',
}

def dashboard(request):
    if request.user.is_authenticated():
        page = request.GET.get('page')
        terminals = Terminal.objects.raw('SELECT * FROM api_terminal')

        context = {
            'terminals': terminals,
        }
        return render(request, 'terminal.html', {**terminalContext, **context})

    else:
        return redirect("/login")
