import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Genre(models.Model):
  genre_text = models.CharField(max_length=200)
  choice_text = models.CharField(max_length=200)

  def __str__(self):
    return self.choice_text

class Song(models.Model):
  song_text = models.CharField(max_length=200)
  date_added = models.DateTimeField('date added')
  likes = models.IntegerField(default=0)
  song_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

  def was_added_recently(self):
    return self.date_added >= timezone.now() - datetime.timedelta(days=1)

  def __str__(self):
    return self.song_text