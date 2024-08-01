from django.urls import reverse
from django.shortcuts import render, redirect

def homepage(request):
    get_user = request.user
    context = {
        'get_user':get_user
    }
    return render (request, 'homepage.html', context)