from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, MessageSerializer
from main.models import Post, Tag, Comment, Profile, Message
from django.contrib.auth.models import User


class UserList(APIView):
	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		print(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		pass

class UserDetail(APIView):
	def get(self, request, username, format=None):
		user = User.objects.get(username=username)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def delete(self, request, username, format=None):
		user = User.objects.get(username=username)
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class View():
	def as_view():
		return HttpResponse()

class Messages(APIView):
	def get(self, request, format=None):
		messages = Message.objects.all()
		serializer = MessageSerializer(messages, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = MessageSerializer(data=request.data)
		print(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageDetail(APIView):
	def get(self, request, id, format=None):
		message = Message.objects.get(pk=id)
		serializer = MessageSerializer(message)
		return Response(serializer.data)

	def delete(self, request, id, format=None):
		message = Message.objects.get(pk=id)
		message.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def put(self, request, id,  format=None):
		message = Message.objects.get(pk=id)
		serializer = MessageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)