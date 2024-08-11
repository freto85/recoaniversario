from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'slideshow'

urlpatterns = [
    path('slidehome/<int:pk>',views.slidehome,name='slidehome'),
    path('create_slideshow/',views.create_slideshow,name='create_slideshow'),
    path('edit_slideshow/<int:pk>',views.edit_slideshow,name='edit_slideshow'),
    path('remove_slideshow/<int:pk>',views.remove_slideshow,name='remove_slideshow'),
    path('add_slide/<int:pk>/',views.add_slide,name='add_slide'),
    path('remove_slide/<int:pk>/',views.remove_slide,name='remove_slide'),
]