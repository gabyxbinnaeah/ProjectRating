from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UpdateProfileForm,ProfileForm,ProjectPostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile,Project 
import datetime as dt

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

# Create your views here.
@login_required(login_url='login')
def index(request):
    date =dt.date.today()
    projects = Project.get_projects()
    return render(request, 'index.html', {"projects":projects})


@login_required(login_url='login')
def post(request):
    '''
    method that post projects 
    '''
    if request.method == 'POST':
        form = ProjectPostForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('index')
    else:
        form = ProjectPostForm()
    return render(request,'post_project.html', {"form":form}) 

@login_required(login_url='login') 
def profile(request):
    '''
    methods that defines profile view
    '''
    current_user=request.user
    profile= Profile.objects.filter(user=current_user).first()
  
    
    return render(request,'profile.html',{"profile":profile,"current_user":current_user})

@login_required(login_url='login')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = UpdateProfileForm()
        return render(request,'edit_profile.html',{"form":form})


@login_required(login_url='login')
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        messages = f"{search_term}"

        return render(request, 'search.html',{"found_project": searched_projects})

    else:
        message = "You haven't searched for any project"
        return render(request, 'search.html',{"message":message})




@login_required(login_url='login')
def get_project_rating(request,id):
    returned_projects = Project.get_project_id(pk=id)
    return render(request, 'index.html', {"returned_projects":returned_projects})


def single_project(request, id):
  projectGot = Project.objects.get(id = id)
  try:
    user_profile = Profile.get_user_profile(request.user.username)
  except UserProfile.DoesNotExist:
    user_profile = None

  if request.method == 'POST':
        design = int(request.POST.get('design'))
        usability = int(request.POST.get('usability'))
        content = int(request.POST.get('content'))
        desc = request.POST.get('rate_description')
        
        new_rate = Rating(design = design, usability= usability, content = content, description = desc , user = request.user_profile, project = projectGot)
        new_rate.save()
        return http.HttpResponseRedirect

  projects_votes=Rating.project_votes(pk=id)
  context = {
    'user_profile':user_profile,
    'projectGot':projectGot,
    'projects_votes':projects_votes,
    
  }
  return render(request, 'project.html', context)

def rating_results(request):
    if request.method == 'POST':
        design = int(request.POST.get('design'))
        usability = int(request.POST.get('usability'))
        content = int(request.POST.get('content'))
        desc = request.POST.get('rate_description')
        
        new_rate = Rating(design = design, usability= usability, content = content, description = desc , user = request.user, project = project)
        new_rate.save()



class MerchList(APIView):
    def get(self, request, format=None):
        all_merch = Project.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    permission_classes = (IsAdminOrReadOnly,) 

class MerchDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_merch(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        merch = self.get_merch(pk)
        serializers = MerchSerializer(merch, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)