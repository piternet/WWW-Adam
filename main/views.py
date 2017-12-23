from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post, Tag
from .forms import PostForm
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger

def index(request):
	posts = Post.objects.all()
	paginator = Paginator(posts,2) #ilosc artykulow na stronie
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
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

def user_info(request, user):
	users = User.objects.get(username=user)
	context =  {'users':users, 'user':user}
	return render(request, 'main/userinfo.html',context)

def add_new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			tags = form.cleaned_data['tag']
			post = form.save(commit=False)
			post.user = request.user
			post.publish_date = datetime.now()
			post.save()
			post.tag.add(*tags)
			post.save()
			return HttpResponseRedirect('/')
	else:
		form = PostForm()
		context = {
			"form": form
		}
		return render(request, 'main/addnewpost.html', context)