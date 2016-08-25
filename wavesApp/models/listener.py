import datetime

from django.db import models
from django.utils import timezone

class Listener(models.Model):
  listener_first_name = models.CharField(max_length=200)
  listener_last_name = models.CharField(max_length=200)

  def __str__(self):
    return self.first_listener_name