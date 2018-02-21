from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
	url(r'^aircountry/$', views.aircountry, name="aircountry")
]