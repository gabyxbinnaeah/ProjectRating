from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views 
from django.urls import  path 

urlpatterns=[
    path('',views.index, name='index'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout/',views.logoutUser,name="logout"),
    path('profile/',views.profile, name="profile"),
    path('edit/',views.edit_profile,name='edit'),
    path('post/', views.post, name="post"),
    path('search/', views.search_results, name="search"),
    path('project/(\d+)/',views.get_project_rating, name="project"),


] 