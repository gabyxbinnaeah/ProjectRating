from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views 
from django.urls import  path 

urlpatterns=[
    path('',views.index, name='index'),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout/',views.logoutUser,name="logout") ,

]