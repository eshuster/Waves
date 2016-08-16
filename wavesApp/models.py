from django.db import models

# Create your models here.


class Genre(models.Model):
    genre_text = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)

class Song(models.Model):
    song_text = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
    likes = models.IntegerField(default=0)
    song_genre = models.ForeignKey(Genre, on_delete=models.CASCADE)