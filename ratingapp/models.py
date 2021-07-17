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

    def __str__(self):
        
        return self.profile_photo.url
    
    def save_profile(self):
        '''
        method that saves  user profile 
        '''
        self.save()
        
    def delete_profile(self):
        '''
        method that deletes user profile 
        '''
        self.delete()
    
    @classmethod   
    def update_bio(cls,id,new_bio):
        '''
        method that updates user profile 
        '''
        cls.objects.filter(pk = id).update(bio=new_bio)
        new_bio_object = cls.objects.get(bio = new_bio)
        new_bio = new_bio_object.bio
        return new_bio


