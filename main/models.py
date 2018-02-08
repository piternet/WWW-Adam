from django.db import models
from django.contrib.auth.models import User
from adamsite.settings import STATIC_URL


class Tag(models.Model):
	name = models.CharField(max_length=200, blank=True, default='', unique=True)

	def __str__(self):
		return self.name


class Post(models.Model):
	title = models.CharField(max_length=300) 
	content = models.CharField(max_length=10000)
	publish_date = models.DateField()
	user = models.ForeignKey(User)
	tag = models.ManyToManyField(Tag)
	photo = models.ImageField(upload_to='main/static/main/imgs/', default='', blank=True)

	def __str__(self):
		return "Tytul: " + self.title + ", Zawartosc: " \
		+ self.content + ", Data: " + self.publish_date.strftime("%d.%m.%Y") \
		+ ", Autor:  " + self.user.username

	class Meta:
		ordering = ['-publish_date', 'title']


class Comment(models.Model):
	content = models.CharField(max_length= 300, blank=True, default='')
	post = models.ForeignKey(Post)
	comment_date = models.DateField()

	def __str__(self):
		return self.content


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.CharField(max_length= 300, blank=True, default='')
	avatar = models.ImageField(upload_to='main/static/main/imgs/', default='', blank=True)
	city = models.CharField(max_length=100, blank=True, default='')
	birth_date = models.DateField(blank=True, null=True)

class Message(models.Model):
	recipient = models.ForeignKey(User, related_name='recipient')
	sender = models.ForeignKey(User, related_name='sender')
	title = models.CharField(max_length= 100, blank=True, default='')
	content = models.CharField(max_length=300, blank=True, default='')
	message_date = models.DateTimeField(null=True)
	readed = models.BooleanField(default=False)

	def __str__(self):
		return self.title