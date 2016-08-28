from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  # This line is required. Links UserProfile to a User model instance.
  user = models.OneToOneField(User)
  name = models.CharField(max_length=50, default = '0')
  # The additional attributes we wish to include.
  # picture = models.ImageField(upload_to='profile_images', blank=True)
  likes = models.IntegerField(default=0)
  spotify_access_token = models.CharField(max_length=100, blank=True)
  soundcloud_access_token = models.CharField(max_length=100, blank=True)
  # Override the __unicode__() method to return out something meaningful!
  def __unicode__(self):
      return self.user.username