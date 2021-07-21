from django.test import TestCase
from .models import Profile,Project,Rating
# Create your tests here.

class ProjectTestClass(TestCase):
    def setUp(self):
        '''
        method that creates instance of image 
        '''
        self.vin= Profile(image="start.pgn",bio="Motivated IT geek")
        self.vin.save_profile()

        self.blog=Project(image="omollo.png",title="omollo",profile=self.vin,likes=700,description="Taken at peak")
        self.blog.save_image()

    def test_image_instance(self):
        '''
        function that checks if image is instanciated 
        '''
        self.assertTrue(isinstance(self.blog,Project))

    def test_save_project(self):
        '''
        Method that test if image model is saved 
        '''
        self.blog.save_project()
        project_list=Image.objects.all()
        self.assertTrue(len(project_list)>0) 

    def test_project_delete(self):
        '''
        method that checks if image is delete_image method deletes image 
        '''
        self.blog.save_image()
        self.blog.delete_project()
        check_list=Project.objects.all()
        self.assertTrue(len(check_list)==0)



class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        Method that creates instance of profile class
        '''
        self.vin= Profile(image="start.pgn",bio="Motivated IT geek")
        self.vin.save_profile()

    def test_instance(self):
        '''
        method that checks if profile is instance
        '''
        self.assertTrue(isinstance(self.vin,Profile))


    def test_save_profile(self):
        '''
        Method that test if profile is being saved
        '''
        self.vin.save_profile()
        list_profile=Profile.objects.all()
        self.assertTrue(len(list_profile)>0) 

    def test_delete_profile(self):
        '''
        method that checks if profile is deleted
        '''
        self.vin.save_profile()
        self.vin.delete_profile()
        left_profiles=Profile.objects.all()
        self.assertTrue(len(left_profiles)==0) 

    def test_bio_update(self):
        '''
        method that checks if bio can be updated
        '''
        self.vin.save_profile()
        self.vin.update_profile_bio( self.vin.id,'Humble motivated coder')
        profile_list=Profile.objects.all()
        self.assertTrue(len(profile_list)==1)
        new_bio=Profile.objects.all().first()
        self.assertTrue(new_bio.bio=='Humble motivated coder')



class RatingTestClass(TestCase):
    '''
    Method that creates instance of Rating class
    '''
    self.votes= Profile(design=4,usability=8,content=9)
    self.votes.save_rating()

