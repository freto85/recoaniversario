from django.db import models
from accounts.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class AudioQuiz(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True) 
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=255, blank=True)
    correct_option = models.IntegerField(default=0)
    comment_1 = models.CharField(max_length=100, blank=True)
    comment_2 = models.CharField(max_length=100, blank=True)
    comment_3 = models.CharField(max_length=100, blank=True)
    comment_4 = models.CharField(max_length=100, blank=True)
    audio_file_1 = models.FileField(upload_to='documents/audio/',validators=[FileExtensionValidator(allowed_extensions=['mp3','wav','ogg'])])
    audio_file_2 = models.FileField(upload_to='documents/audio/',validators=[FileExtensionValidator(allowed_extensions=['mp3','wav','ogg'])])
    audio_file_3 = models.FileField(upload_to='documents/audio/',validators=[FileExtensionValidator(allowed_extensions=['mp3','wav','ogg'])])
    audio_file_4 = models.FileField(upload_to='documents/audio/',validators=[FileExtensionValidator(allowed_extensions=['mp3','wav','ogg'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.title