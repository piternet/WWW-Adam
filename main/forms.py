from django import forms
from .models import Post, Tag, Comment

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

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'post']
		widgets = {
			'content': forms.Textarea(attrs={'cols': 30 , 'rows': 20})
		}
		labels = {
			'post': 'post',
			'content': 'Zawartosc'
		}