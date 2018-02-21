from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Post, Tag, Comment, Profile, Message
from django.contrib.auth.models import User

def aircountry(request):
	tags = Tag.objects.all()
	context = {
		'tag': tags
	}
	return render(request, 'main/air_country.html', context)
