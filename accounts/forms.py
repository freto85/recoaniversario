from django import forms

from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','password1','password2')
        model = User        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = "Nombre de Usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar Contraseña"