from django import forms
from video.models import VideoModel

class VideoForm(forms.ModelForm):

    class Meta():
        model = VideoModel
        fields = ('title','video_url','video_file','description')

        widgets = {
            'title':forms.TextInput(attrs={'class':'texinputclass'}),
        }
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].label = "Título"
        self.fields['video_url'].label = "Video URL"
        self.fields['video_file'].label = "Archivo de Video"
        self.fields['video_file'].required = False
        self.fields['description'].label = "Descripción"