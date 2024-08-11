from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from slideshow.models import Slideshow
from video.models import VideoModel
from musica.models import AudioQuiz

def homepage(request):
    get_user = request.user
    if get_user.is_authenticated:
        get_slideshow = Slideshow.objects.all()
        get_video = VideoModel.objects.all()
        get_quiz = AudioQuiz.objects.all()
    if request.method == "POST":
        get_username = request.POST.get('login-username')
        get_password = request.POST.get('login-password')
        get_authentication = authenticate(username=get_username,password=get_password)
        print(get_authentication)
        if get_authentication is not None:
            login(request, get_authentication)
            return redirect('homepage')
    if get_user.is_authenticated:
        context = {
            'get_user':get_user,
            'get_slideshow':get_slideshow,
            'get_video':get_video,
            'get_quiz':get_quiz,
        }
    else:
        context = {
            'get_user':get_user,
        }
    return render (request, 'homepage.html', context)