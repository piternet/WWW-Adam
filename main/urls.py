from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tags/', views.tags, name='tags'),
	url(r'^tag/(?P<name>\w+)/$', views.tag_view, name='tag_view'),
	url(r'^user/(?P<user>\w+)/$', views.user_info, name='user_info'),
	url(r'^post/(?P<id>\d+)/$', views.one_post, name='one_post'),
	url(r'^login/', login, name='login'),
	url(r'^logout/', logout, name='logout')
]
