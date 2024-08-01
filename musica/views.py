from django.shortcuts import render

# Create your views here.

def musica_start(request):
    get_user = request.user
    context = {
        'get_user':get_user
    }
    return render(request,'musica/actividad/musica_start.html', context)