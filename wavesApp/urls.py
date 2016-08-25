from django.conf.urls import url
from . import views
from . import models

app_name = 'wavesApp'
urlpatterns = [
  url(r'^$', views.song.index, name='index'),
  url(r'^register/$', views.user_profile.register, name='register'),
  url(r'^login/$', views.user_profile.user_login, name='user_login'),
  url(r'^logout/$', views.user_profile.user_logout, name='user_logout'),
  url(r'^(?P<song_id>[0-9]+)/$', views.song.detail, name='detail'),
]