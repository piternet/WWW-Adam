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
	# 1. pobrac z bazy danych tag o nazwie name
	# 2. pobrac z bazy danych wszystkie posty, ktore maja naszego taga
		# Post.objects.filter()
	# 3. zrobic szablon dla taga
	# 4. przekazac do funkcji render ten szablon i odpowiedni context
	return render(request, 'main/tag1.html', context)

