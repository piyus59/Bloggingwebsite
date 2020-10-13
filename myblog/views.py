from django.shortcuts import render
from . models import Blog,Category

# Create your views here.

def createblog(request):
	if request.method == 'POST':
		title = request.POST['title']
		text = request.POST['blog']
		print(title,text)

	cats = Category.objects.all()
	return render(request, 'blog.html', {'cats':cats})

def index(request):
	return render(request, 'index.html')
