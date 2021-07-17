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


class Project(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    image=CloudinaryField('image',blank=True,null=True)
    description=models.TextField(max_length=400,null=True)
    date_created=models.DateTimeField(default=timezone.now)
    link=models.URLField() 
    title=models.CharField(max_length=100,null=True) 

    def save_project(self):
        self.save()

    def projects(cls):
        '''
        method that return all projects
        '''
        projects=csl.objects.all()
        return projects
    
    def project_url(self):
        '''
        method that retuns project url
        '''

        if self.project and hasattr(self.project, 'url'):
            return self.project.url

    def delete_project(self):
        '''
        method that deletes specified project using project id 
        '''
        self.delete()
       

    @classmethod
    def update_project(cls,old,new):
        '''
        method that updates project
        '''
        cap = Project.objects.filter(caption=old).update(caption=new)
        return cap

    @classmethod
    def search_project(cls, title):
        '''
        method that filters project by title
        '''
        return cls.objects.filter(title__icontains=title).all()

    def __str__(self):
        return str(self.title) if self.title else ''

    



    
    






