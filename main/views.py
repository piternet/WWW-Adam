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

