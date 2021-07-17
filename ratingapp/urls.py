from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views  

urlpatterns=[
    url('',views.index, name='index'),
    url('register/', views.registerPage, name="register"),
	url('login/', views.loginPage, name="login"), 
    url('logout/',views.logoutUser,name="logout") ,

]