from django.shortcuts import render,redirect
from slideshow.forms import SlideshowForm
from slideshow.models import Slideshow,Picture

# Create your views here.

def slidehome(request,pk):
    get_user = request.user
    get_album = Slideshow.objects.get(pk=pk)
    get_pictures = Picture.objects.filter(slideshow=get_album).order_by('position')
    context = {
        'get_user':get_user,
        'get_album':get_album,
        'get_pictures':get_pictures,
    }
    return render(request,'slideshow/slidehome.html', context)

def create_slideshow(request):
    get_user=request.user
    if request.method == 'POST':
        get_form = SlideshowForm(request.POST,request.FILES)
        if get_form.is_valid():
            print("not error")
            finished_form = get_form.save()
            finished_form.user = get_user
            finished_form.save()
            return redirect('homepage')
    else:
        get_form = SlideshowForm()
    context = { 
        'get_form': get_form,
        'get_user':get_user
    }
    return render(request,'slideshow/create_slideshow.html', context)

def add_slide(request,pk):
    get_user=request.user
    get_slideshow = Slideshow.objects.get(pk=pk)
    get_slides = Picture.objects.filter(slideshow=get_slideshow)
    slide_order = []
    slide_index = 0
    for slide in get_slides:
        slide_order.append(slide.position)
    if len(slide_order) > 0:
        slide_index = max(slide_order)
    if request.method == 'POST':
        get_image = request.FILES.get('input-image')
        get_text = request.POST.get('input-text')
        Picture.objects.create(user=get_user,slideshow=get_slideshow,description=get_text,image_field=get_image,position=slide_index)
        return redirect('slideshow:slidehome', pk=pk)
    else:
        get_form = SlideshowForm()
    context = { 
        'get_form': get_form,
        'get_user':get_user,
        'get_slideshow':get_slideshow,
    }
    return render(request,'slideshow/add_slide.html', context)

def remove_slide(request,pk):
    get_user=request.user
    get_picture = Picture.objects.get(pk=pk)
    slideshow_pk = get_picture.slideshow.pk
    if request.method == "POST":
        get_picture.delete()
        get_pictures = Picture.objects.filter(slideshow=get_picture.slideshow).order_by('position')
        if len(get_pictures) > 0:
            index = 0
            for picture in get_pictures:
                picture.position = index
                picture.save()
                index = index + 1
        return redirect('slideshow:slidehome', pk=slideshow_pk)
    context = { 
        'get_user':get_user,
        'get_picture':get_picture,
    }
    return render(request,'slideshow/remove_slide.html', context)

def edit_slideshow(request,pk):
    get_user = request.user
    get_slideshow = Slideshow.objects.get(pk=pk)
    if request.method == 'POST':
        get_form = SlideshowForm(request.POST,instance=get_slideshow)
    else:
        get_form= SlideshowForm(instance=get_slideshow)
    context = {
        'get_user':get_user,
        'get_form':get_form,
    }
    return render(request,'slideshow/edit_slideshow.html', context)

def remove_slideshow(request,pk):
    get_user = request.user
    get_slideshow = Slideshow.objects.get(pk=pk)
    get_slides = Picture.objects.filter(slideshow=get_slideshow)
    if request.method == "POST":
        for slide in get_slides:
            slide.delete()
        get_slideshow.delete()
        return redirect('homepage')
    context = {
        'get_user':get_user,
        'get_slideshow':get_slideshow,
    }
    return render(request,'slideshow/remove_slideshow.html', context)

