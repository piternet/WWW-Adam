from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
	url(r'^aircountry/$', views.aircountry, name="aircountry"),
	url(r'^aircountry/(?P<country>[\w -:]+)/$', views.aircity, name='aircity'),
	url(r'^aircountry/(?P<country>[\w -:]+)/(?P<city>[\w -:]+)/$', views.airlocation, name='airlocation'),
	url(r'^aircountry/(?P<country>[\w -:]+)/(?P<city>[\w -:]+)/(?P<location>[\w -:]+)/$', views.latestmeasure, name='latestmeasure')
]