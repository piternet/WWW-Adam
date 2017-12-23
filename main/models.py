from django.db import models
from django.contrib.auth.models import User


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

	def __str__(self):
		return "Tytul: " + self.title + ", Zawartosc: " \
		+ self.content + ", Data: " + self.publish_date.strftime("%d.%m.%Y") \
		+ ", Autor:  " + self.user.username

	class Meta:
		ordering = ['-publish_date', 'title']


class Comment(models.Model):
	content = models.CharField(max_length= 300, blank=True, default='')
	post = models.ForeignKey(Post)

	def __str__(self):
		return self.content



