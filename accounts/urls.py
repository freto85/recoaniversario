from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign_out/', views.sign_out,name='sign_out'),
    path('sign_up/',views.sign_up,name='sign_up'),

    
]