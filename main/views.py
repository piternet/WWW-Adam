from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Post, Tag, Comment, Profile
from .forms import PostForm, CommentForm, TagForm, ProfileForm
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger
from adamsite.settings import POSTS_PER_PAGE
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models.signals import post_save

def index(request):
	posts = Post.objects.all()
	comments = Comment.objects.all()
	paginator = Paginator(posts, POSTS_PER_PAGE) #ilosc artykulow na stronie
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	context = {
		'posts': posts,
		'comments': comments
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

def post_list(request, name):
	tags = Tag.objects.all()
	posts = Post.objects.filter(tag__name='#'+name)
	context = {'posts':posts, 'name':name}
	return render(request, 'main/post_list.html', context)

def one_post(request, id):
	post1 = Post.objects.get(id=id) #czemu nie dziala filter tutaj
	context = {'post1':post1, 'id':id}
	return render(request, 'main/onepost.html',context)

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        f = UserCreationForm()
    return render(request, 'main/register.html', {'form': f})

@login_required(login_url='/login/')
def user_info(request, user):
	users = User.objects.get(username=user)
	try:
		profile = Profile.objects.get(user=users) #nie wiem jak pobrac jeden gdzie user=user
	except Profile.DoesNotExist:
		profile = None
	context =  {'users':users, 'user':user, 'profile':profile}
	return render(request, 'main/userinfo.html',context)

@login_required(login_url='/login/')
def add_new_comment(request, id):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.comment_date = datetime.now()
			comment.post = Post.objects.get(id=int(id))
			comment.save()
			return HttpResponseRedirect('/')
	else:
		form = CommentForm()
		context = {
			"form": form
		}
		return render(request, 'main/addcomment.html', context)

@login_required(login_url='/login/?failed=1')
def add_new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
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

@login_required(login_url='/login/')
def remove_post(request,id, template_name='main/confirm_delete_post.html'):
    post = get_object_or_404(Post, pk=id)
    if request.user.id != post.user.id:
    	return redirect('index')
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'id':id})

def add_new_tag(request):
	if request.method == 'POST':
		form = TagForm(request.POST)
		if form.is_valid():
			tag = form.save(commit=False)
			tag.save()
			return HttpResponseRedirect('/')
	else:
		form = TagForm()
		context = {
			"form": form
		}
		return render(request, 'main/addnewtag.html', context)

def edit_post(request, id):
	post = Post.objects.get(id=int(id))
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post.title = form.cleaned_data['title']
			post.photo = form.cleaned_data['photo']
			post.content = form.cleaned_data['content']
			tag = form.cleaned_data['tag']
			post.tag.clear()
			post.tag.add(*tag)
			post.save()
			return HttpResponseRedirect('/')

	else:
		form = PostForm(initial={
			'title': post.title,
			'content': post.content,
			'tag': post.tag.all()
		})
		context = {
			'form': form,
			'post': post
		}
		return render(request, 'main/editpost.html', context)

def edit_profile(request):
	profile = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.description = form.cleaned_data['description']
			profile.avatar = form.cleaned_data['avatar']
			profile.city = form.cleaned_data['city']
			profile.birth_date = form.cleaned_data['birth_date']
			profile.save()
			return HttpResponseRedirect('/')
	else:
		form = ProfileForm(initial={
			'description': profile.description,
			'city': profile.city,
			'birth_date': profile.birth_date
		})
		context = {
			'form': form,
			'profile': profile
		}
		return render(request, 'main/editprofile.html', context)

def create_profile(sender, **kwargs):
	user = kwargs['instance']
	if kwargs['created']:
		profile = Profile(user=user)
		profile.save()

post_save.connect(create_profile, sender=User)