from django.db import models
from accounts.models import User
from django.core.validators import FileExtensionValidator
from django_resized import ResizedImageField

# Create your models here.

class Slideshow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    image_field = ResizedImageField(size=[1024, 768], crop=['middle', 'center'], upload_to='documents/image/slide/title',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Picture(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    slideshow = models.ForeignKey(Slideshow,on_delete=models.CASCADE,null=True)
    description = models.TextField(max_length=255, blank=True)
    image_field = ResizedImageField(size=[1024, 768], crop=['middle', 'center'], upload_to='documents/image/slide',null=True)
    position = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
