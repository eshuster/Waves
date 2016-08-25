import datetime

from django.db import models
from wavesApp.models.playlist import Playlist
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
  genre_name = models.CharField(max_length=200)
  playlists = models.ManyToManyField(Playlist)

  def __str__(self):
    return self.genre_name
