from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages

def login_view(request):
    if(request.user.is_authenticated()):
        return redirect("/event")

    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/event")

    return render(request, "form.html", {"form":form, "title":title} )

def register_view(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        user = authenticate(username=user.username, password=password)
        login(request, user)
        messages.success(request, "You are now registered!")
        return redirect("/event")
    else:
        MESSAGE_TAGS = {
            messages.ERROR: 'danger'
        }
        messages.error(request, "Something happened. Please correct the errors below.")

    return render(request, "form.html", {"form": form, "title": title})

def logout_view(request):
    logout(request)
    return redirect("/")
