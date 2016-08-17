from django.conf.urls import url
from . import views

app_name = 'wavesApp'
urlpatterns = [
  # ex: /wavesApp/
  url(r'^$', views.index, name='index'),
  # ex: /wavesApp/5/
  url(r'^(?P<song_id>[0-9]+)/$', views.detail, name='detail'),
  # ex: /wavesApp/5/results/
  url(r'^(?P<song_id>[0-9]+)/results/$', views.results, name='results'),
  # ex: /wavesApp/5/vote/
  url(r'^(?P<song_id>[0-9]+)/vote/$', views.vote, name='vote'),
]