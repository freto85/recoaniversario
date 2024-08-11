from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'musica'

urlpatterns = [
    path('start/<int:pk>',views.musica_start,name='musica_start'),
    path('create_audio_quiz/',views.create_audio_quiz,name='create_audio_quiz'),
    path('edit_quiz/<int:pk>',views.edit_quiz,name='edit_quiz'),
    path('remove_quiz/<int:pk>',views.remove_quiz,name='remove_quiz'),
    path('quiz_answer/<int:pk>/<str:option>',views.quiz_answer,name='quiz_answer'),
]