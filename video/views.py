from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from video.forms import VideoForm
from video.models import VideoModel

# Create your views here.


@login_required
def create_video(request):
    get_user=request.user
    if request.method == 'POST':
        get_form = VideoForm(request.POST,request.FILES)
        if get_form.is_valid():
            finished_form = get_form.save()
            finished_form.user = get_user
            finished_form.save()
            return redirect('homepage')
    else:
        get_form = VideoForm()
    context = { 
        'get_form': get_form,
        'get_user':get_user
    }
    return render(request,'video/create_video.html', context)

def video_detail(request,pk):
    get_user = request.user
    get_video = VideoModel.objects.get(pk=pk)
    print(get_video.video_file)
    context = {
        'get_user':get_user,
        'get_video':get_video,
    }
    return render(request,'video/video_detail.html', context)

def edit_video(request,pk):
    get_user = request.user
    get_video = VideoModel.objects.get(pk=pk)
    if request.method == 'POST':
        get_form = VideoForm(request.POST,request.FILES,instance=get_video)
        if get_form.is_valid():
            print("valid!")
            finished_form = get_form.save()
            return redirect('homepage')
    else:
        get_form= VideoForm(instance=get_video)
    context = {
        'get_user':get_user,
        'get_form':get_form,
    }
    return render(request,'video/edit_video.html', context)

def remove_video(request,pk):
    get_user=request.user
    get_video = VideoModel.objects.get(pk=pk)
    if request.method == 'POST':
        get_video.delete()
        return redirect('homepage')
    context = {
        'get_user':get_user,
        'get_video':get_video,
    }
    return render(request,'video/remove_video.html', context)

