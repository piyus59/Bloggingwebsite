from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from . models import Blog,Category
from django.contrib.auth.models import User, auth

# Create your views here.


def createblog(request):
	if request.user.is_authenticated:
		print(request.user.username)
	if request.method == 'POST':
		title = request.POST['title']
		text = request.POST['blog']
		category = request.POST['category']
		messages.info(request,(title,text,category, request.user.username))

		blogobj = Blog()
		blogobj.title = title
		blogobj.text = text
		blogobj.category_id = category
		blogobj.user_id = request.user.id
		blogobj.save()
		return HttpResponseRedirect('/')

	cats = Category.objects.all()
	
	return render(request, 'blog.html', {'cats':cats})

def index(request):
	request_dict = request.GET
	if request_dict.get('show_cat'):
		shows = Category.objects.all()
		blogs = Blog.objects.filter(category_id=request_dict.get('show_cat'))
	else:
		shows = Category.objects.all()
		blogs = Blog.objects.all()
	return render(request, 'index.html', {'blogs':blogs, 'shows':shows})


