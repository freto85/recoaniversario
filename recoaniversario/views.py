from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

def homepage(request):
    get_user = request.user
    if request.method == "POST":
        get_username = request.POST.get('login-username')
        get_password = request.POST.get('login-password')
        get_authentication = authenticate(username=get_username,password=get_password)
        print(get_authentication)
        if get_authentication is not None:
            login(request, get_authentication)
            return redirect('homepage')
    context = {
        'get_user':get_user
    }
    return render (request, 'homepage.html', context)