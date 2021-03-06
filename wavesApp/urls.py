from django.conf.urls import url
from . import views
from . import models

app_name = 'wavesApp'
urlpatterns = [
  url(r'^$', views.base.index, name='index'),
  url(r'^register/$', views.user_profile.register, name='register'),
  url(r'^login/$', views.user_profile.user_login, name='user_login'),
  url(r'^logout/$', views.user_profile.user_logout, name='user_logout'),
  url(r'^sc_login/?$', views.sound_cloud.sc_login, name='sc_login'),
  url(r'^to_sc_login/?$', views.sound_cloud.to_sc_login, name='to_sc_login'),
  url(r'^spotify_login/?$', views.spotify.spotify_login, name='spotify_login'),
  url(r'^to_spotify_login/?$', views.spotify.to_spotify_login, name='to_spotify_login'),
  url(r'^current_user/?$', views.spotify.current_user, name='current_user'),
  url(r'^user_info/?$', views.sound_cloud.user_info, name='user_info'),
  url(r'^(?P<song_id>[0-9]+)/$', views.song.detail, name='detail'),
]