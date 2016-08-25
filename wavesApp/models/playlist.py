import datetime

from django.db import models
from django.utils import timezone

class Playlist(models.Model):
  playlist_name = models.CharField(max_length=200)
  likes = models.IntegerField(default=0)

  def __str__(self):
    return self.playlist_name