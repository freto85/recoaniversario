from django.shortcuts import render,redirect
from musica.models import AudioQuiz

# Create your views here.

def musica_start(request,pk):
    get_user = request.user
    get_quiz = AudioQuiz.objects.get(pk=pk)
    if request.method == "POST":
        get_answer = request.POST.get('music-answer')
        if int(get_answer) == get_quiz.correct_option:
            return redirect('musica:quiz_answer',pk=get_quiz.pk,option="correcta")
        else:
            return redirect('musica:quiz_answer',pk=get_quiz.pk,option="incorrecta")
    context = {
        'get_user':get_user,
        'get_quiz':get_quiz,
    }
    return render(request,'musica/actividad/musica_start.html', context)

def create_audio_quiz(request):
    get_user = request.user
    if request.method == "POST":
        get_title = request.POST.get('input-title')
        get_description = request.POST.get('input-description')
        get_audio_1 = request.FILES.get('file-1')
        get_comment_1 = request.POST.get('text-1')
        get_audio_2 = request.FILES.get('file-2')
        get_comment_2 = request.POST.get('text-2')
        get_audio_3 = request.FILES.get('file-3')
        get_comment_3 = request.POST.get('text-3')
        get_audio_4 = request.FILES.get('file-4')
        get_comment_4 = request.POST.get('text-4')
        get_correct_answer = request.POST.get('correct-answer')
        get_feedback = request.POST.get('input-feedback')
        AudioQuiz.objects.create(title=get_title,description=get_description,correct_option=get_correct_answer,comment_1=get_comment_1,comment_2=get_comment_2,comment_3=get_comment_3,comment_4=get_comment_4,audio_file_1=get_audio_1,audio_file_2=get_audio_2,audio_file_3=get_audio_3,audio_file_4=get_audio_4,feedback=get_feedback)
        return redirect('homepage')
    context = {
        'get_user':get_user
    }
    return render(request,'musica/actividad/create_audio_quiz.html', context)

def edit_quiz(request,pk):
    get_user = request.user
    get_quiz = AudioQuiz.objects.get(pk=pk)
    context = {
        'get_user':get_user,
        'get_quiz':get_quiz,
    }
    return render(request,'musica/actividad/edit_quiz.html', context)

def remove_quiz(request,pk):
    get_user = request.user
    get_quiz = AudioQuiz.objects.get(pk=pk)
    if request.method == "POST":
        get_quiz.delete()
        return redirect('homepage')
    context = {
        'get_user':get_user,
        'get_quiz':get_quiz,
    }
    return render(request,'musica/actividad/remove_quiz.html', context)

def quiz_answer(request,pk,option):
    get_user = request.user
    get_quiz = AudioQuiz.objects.get(pk=pk)
    get_option = option
    context = {
        'get_user': get_user,
        'get_quiz': get_quiz,
        'get_option': get_option,
    }
    return render(request,'musica/actividad/quiz_answer.html',context)