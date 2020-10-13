from django.urls import path
	
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('myblog/createblog',views.createblog, name='blog')
]