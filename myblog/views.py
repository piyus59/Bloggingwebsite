from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from . models import Blog,Category
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

	# user_list = Blog.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(blogs, 2)

	try:
		Items = paginator.page(page)
	except PageNotAnInteger:
		Items = paginator.page(1)
	except EmptyPage:
		Items = paginator.page(paginator.num_pages)
	return render(request, 'index.html', {'shows':shows, 'Items':Items})

def personalblogs(request):
	
	blogs = Blog.objects.filter(user_id=request.user)
	return render(request, 'personalblogs.html', {'blogs':blogs})


def delete(request):
    print('piuni		',request.POST['blogid'])
    blog = get_object_or_404(Blog,id = request.POST['blogid'])
    bloger = blog.user.username
    print("dsdsdsd			",bloger)
    if request.method == 'POST' and request.user.is_authenticated and request.user.username == bloger:
	    blog.delete()
	    messages.success(request, "Post Successfully deleted!")
	    return HttpResponseRedirect('/myblog/personalblogs')
    return HttpResponseRedirect(request, '/', {'blog':blog, 'bloger':bloger})


