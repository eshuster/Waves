from django.conf.urls import url
from . import views
from . import models

app_name = 'wavesApp'
urlpatterns = [
  url(r'^$', views.song.index, name='index'),
  url(r'^register/$', views.user_profile.register, name='register'),
  url(r'^login/$', views.user_profile.user_login, name='user_login'),
  url(r'^logout/$', views.user_profile.user_logout, name='user_logout'),
  url(r'^sc_login/?$', views.sound_cloud.sc_login, name='sc_login'),
  url(r'^to_sc_login/?$', views.sound_cloud.to_sc_login, name='to_sc_login'),
  url(r'^spotify_login/?$', views.spotify.spotify_login, name='spotify_login'),
  url(r'^to_spotify_login/?$', views.spotify.to_spotify_login, name='to_spotify_login'),
  url(r'^get_liked_songs/?$', views.spotify.get_liked_songs, name='get_liked_songs'),
  url(r'^(?P<song_id>[0-9]+)/$', views.song.detail, name='detail'),
]