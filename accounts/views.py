from django.shortcuts import render,redirect
from django.contrib.auth import logout
from accounts.forms import UserCreateForm


# Create your views here.

def sign_out(request):
    get_user = request.user
    logout(request)
    return redirect('homepage')

def sign_up(request):
    get_user = request.user
    if request.method == "POST":
        get_form = UserCreateForm(request.POST)
        if get_form.is_valid():
            finished_form = get_form.save()
            print(finished_form)
            return redirect('homepage')
    else:
        get_form = UserCreateForm()
    context = {
        'get_user':get_user,
        'get_form':get_form,
    }
    return render (request, 'accounts/sign_up.html', context)
    