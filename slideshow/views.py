from django.shortcuts import render

# Create your views here.

def slidehome(request):
    get_user = request.user
    context = {
        'get_user':get_user
    }
    return render(request,'slideshow/slidehome.html', context)

def create_slideshow(request):
    get_user = request.user
    context = {
        'get_user':get_user
    }
    return render(request,'slideshow/create_slideshow.html', context)