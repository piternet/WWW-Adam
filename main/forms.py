from django import forms
from .models import Post, Tag, Comment, Profile

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'tag']
		widgets = {
			'content': forms.Textarea(attrs={'cols': 30 , 'rows': 20})
		}
		labels = {
			'title': 'Tytul',
			'content': 'Zawartosc'
		}

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['name']
		widgets = {
			'name': forms.Textarea(attrs={'cols': 30 , 'rows': 1})
		}
		labels = {
			'name': 'Nazwa',
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
		widgets = {
			'content': forms.Textarea(attrs={'cols': 30 , 'rows': 20})
		}
		labels = {
			'content': 'Zawartosc'
		}

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['description', 'avatar', 'city', 'birth_date']
		widgets = {
			'description': forms.Textarea(attrs={'cols': 30 , 'rows': 10}),
			'birth_date': forms.SelectDateWidget(years=range(1900,2020))
		}