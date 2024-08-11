from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'slideshow'

urlpatterns = [
    path('video_detail/<int:pk>',views.video_detail,name='video_detail'),
    path('create_video/',views.create_video,name='create_video'),
    path('edit_video/<int:pk>',views.edit_video,name='edit_video'),
    path('remove_video/<int:pk>',views.remove_video,name='remove_video'),
]