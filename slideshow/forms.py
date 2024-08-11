from django import forms
from slideshow.models import Slideshow

class SlideshowForm(forms.ModelForm):
    class Meta():
        model = Slideshow
        fields = ('title','image_field')

        widgets = {
            'title':forms.TextInput(attrs={'class':'texinputclass'}),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label = "Título"
        self.fields['image_field'].label = "Portada"