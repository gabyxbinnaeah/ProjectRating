import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone 
from django.dispatch import receiver

class Profile(models.Model):
    '''
    model that defines profile fields
    '''
    image = CloudinaryField('image', blank=True, null=True)
    bio = models.TextField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)



