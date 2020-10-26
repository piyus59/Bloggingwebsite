from django.urls import path
	
from . import views

urlpatterns = [
	path('register',views.register, name='register'),
	path('login' ,views.login, name='login'),
	path('logout' ,views.logout, name='logout'),
	path('index' ,views.index, name='index'),
	path('about' ,views.about,name='about'),
	path('contact' ,views.contact,name='contact')
]