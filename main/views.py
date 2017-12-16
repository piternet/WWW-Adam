from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag

def index(request):
	posts = Post.objects.all()
	context = {
		'posts': posts
	}
	return render(request, 'main/index.html', context)

def tags(request):
	tags = Tag.objects.all()
	context = {
		'tag': tags
	}
	return render(request, 'main/tags.html', context)

def tag_view(request, name):
	tags = Tag.objects.all()
	posts = Post.objects.filter(tag__name='#'+name)
	context = {'posts':posts, 'name':name}
	return render(request, 'main/tag1.html', context)

def one_post(request, id):
	post1 = Post.objects.get(id=id) #czemu nie dziala filter tutaj
	context = {'post1':post1, 'id':id}
	return render(request, 'main/onepost.html',context)

