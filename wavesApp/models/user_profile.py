from django.db import models
from django.contrib.auth.models import User
import spotipy

class UserProfile(models.Model):
  # This line is required. Links UserProfile to a User model instance.
  user = models.OneToOneField(User)
  name = models.CharField(max_length=50, default = '0')
  # The additional attributes we wish to include.
  # picture = models.ImageField(upload_to='profile_images', blank=True)
  likes = models.IntegerField(default=0)
  spotify_access_token = models.CharField(max_length=100, blank=True)
  soundcloud_access_token = models.CharField(max_length=100, blank=True)

  soundcloud_user_id = models.CharField(max_length=100, blank=True)
  soundcloud_username = models.CharField(max_length=100, blank=True)
  soundcloud_user_track_count = models.CharField(max_length=100, blank=True)
  soundcloud_user_playlist_count = models.CharField(max_length=100, blank=True)
  soundcloud_user_public_favorites_count = models.CharField(max_length=100, blank=True)
  soundcloud_user_private_tracks_count = models.CharField(max_length=100, blank=True)
  soundcloud_user_private_playlists_count = models.CharField(max_length=100, blank=True)

  spotify_user_id = models.CharField(max_length=100, blank=True)
  spotify_user_display_name = models.CharField(max_length=100, blank=True)
  spotify_user_external_urls = models.CharField(max_length=100, blank=True)
  spotify_user_followers = models.CharField(max_length=100, blank=True)

  def get_liked_songs(user):
    current_user = user
    current_user_profile = UserProfile.objects.get(user=current_user)
    spotify_access_token = current_user_profile.spotify_access_token

    if spotify_access_token:
      sp = spotipy.Spotify(auth=spotify_access_token)
      results = sp.current_user_saved_tracks()
      for item in results['items']:
          track = item['track']
          print(track['name'] + ' - ' + track['artists'][0]['name'])
    return results

  def current_user(user):
    current_user = user
    current_user_profile = UserProfile.objects.get(user=current_user)
    spotify_access_token = current_user_profile.spotify_access_token
    sp = spotipy.Spotify(auth=spotify_access_token)
    results = sp.current_user_top_tracks()
    print(results)
    return results

  # Override the __unicode__() method to return out something meaningful!
  def __unicode__(self):
      return self.user.username