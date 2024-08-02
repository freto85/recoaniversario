from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'musica'

urlpatterns = [
    path('slidehome/',views.slidehome,name='slidehome'),
    path('create_slideshow/',views.create_slideshow,name='create_slideshow'),
]