from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'musica'

urlpatterns = [
    path('start/',views.musica_start,name='musica_start'),
    path('create_audio_quiz/',views.create_audio_quiz,name='create_audio_quiz'),
]