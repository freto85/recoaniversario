from django.db import models
from embed_video.fields import EmbedVideoField
from accounts.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class VideoModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    video_url = EmbedVideoField()
    video_file = models.FileField(upload_to='documents/video/',validators=[FileExtensionValidator(allowed_extensions=['mp4','avi'])],blank=True,null=True)
    slug = models.SlugField(max_length=200, db_index=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
