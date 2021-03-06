from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,Project,Rating 


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['user'] 

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['image','bio']


class ProjectPostForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['date_created','author'] 


# class  RatingForm(forms.ModelForm):
#     class Meta:

#         model=Rating
#         exclude=['user_profile','project'] 

    

    

