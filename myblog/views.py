from django.shortcuts import render
from . models import Blog

# Create your views here.


def createblog(request):
	if request.method == 'Post':
		title = request.post['title']
		text = request.post['text']
	cats = Blog.category
	print("===============================")
	print(dir(cats))

	return render(request, 'blog.html')

def index(request):
	return render(request, 'index.html')
