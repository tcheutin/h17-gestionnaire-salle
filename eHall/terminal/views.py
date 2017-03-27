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
        terminals = getTerminalPage(request, page)

        context = {
            'termials': terminals
        }
        return render(request, 'terminal.html', {**terminalContext, **context})
    else:
        return redirect("/login")


def getTerminalPage(request, page):
    user = request.user
    terminals = Terminal.objects.all().order_by('-id') if request.user.is_superuser else Terminal.objects.filter(creator=user.id).order_by('-id')
    paginator = Paginator(terminals, 10) # Show 10 terminals per page

    try:
        # Display the requested page
        terminals = paginator.page(page)
    except PageNotAnInteger:
        # Display the first page if no valid page argument is provided
        terminals = paginator.page(1)
    except EmptyPage:
        # Display the last page if the requested range exceeds the number of entries
        terminals = paginator.page(paginator.num_pages)

    return terminals
