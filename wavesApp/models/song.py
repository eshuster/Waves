import datetime

from django.db import models
from wavesApp.models.genre import Genre
from django.utils import timezone

class Song(models.Model):
  song_name = models.CharField(max_length=200)
  likes = models.IntegerField(default=0)
  genres = models.ManyToManyField(Genre)

  def __str__(self):
    return self.song_name
