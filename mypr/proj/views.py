from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect



@login_required
def view_go(request):

    return render(request, "index.html")


def user_login(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect("main_page")
        else:
            messages.error(request, 'No entry allowed')
    return render(request, "login.html")


def user_logout(request):
    pass
