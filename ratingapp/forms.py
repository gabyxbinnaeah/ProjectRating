from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,Project,rating_content_object,rating_design_object,rating_usability_object


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


class  ContentForm(forms.ModelForm):
    class Meta:

        model=rating_content_object
        fields=['rate','description']

class  DesignForm(forms.ModelForm):
    class Meta:

        model=rating_design_object
        fields=['rate','description']

class  UsabilityForm(forms.ModelForm):
    class Meta:

        model=rating_usability_object
        fields=['rate','description']
    

