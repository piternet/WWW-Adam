from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^tags/', views.tags, name='tags'),
	url(r'^tag/(?P<name>\w+)/$', views.tag_view, name='tag_view'),
	url(r'^bytag/(?P<name>\w+)/$', views.post_list, name='post_list'),
	url(r'^user/(?P<user>\w+)/$', views.user_info, name='user_info'),
	url(r'^post/(?P<id>\d+)/$', views.one_post, name='one_post'),
	url(r'^add_new_post/$', views.add_new_post, name="add_new_post"),
	url(r'^remove_post/(?P<id>\d+)/$', views.remove_post, name="remove_post"),
	url(r'^edit_post/(?P<id>\d+)/$', views.edit_post, name="edit_post"),
	url(r'^add_new_comment/(?P<id>\d+)/$', views.add_new_comment, name="add_new_comment"),
	url(r'^add_new_tag/$', views.add_new_tag, name="add_new_tag"),
	url(r'^login/', login, name='login'),
	url(r'^register/', views.register, name='register'),
	url(r'^logout/', logout, name='logout'),
	url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
	url(r'^sendmessage/$', views.send_message, name="sendmessage"),
]