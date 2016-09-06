from django.http                    import HttpResponseRedirect, HttpResponse
from django.conf                    import settings
from wavesApp.models.user_profile   import UserProfile

from pprint import pprint



import urllib, cgi, simplejson
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import requests

def to_spotify_login(request):
  current_user = request.user

  scope = 'playlist-modify'
  # scope = 'user-library-read'

  if len(sys.argv) > 1:
    username = sys.argv[1]
  else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

  token = util.prompt_for_user_token(username, scope,
                        client_id=settings.SPOTIFY_CLIENT_ID,
                        client_secret=settings.SPOTIFY_CLIENT_SECRET,
                        redirect_uri='http://127.0.0.1:8000/wavesApp/spotify_login')

  current_user_profile = UserProfile.objects.get(user=current_user)
  current_user_profile.spotify_access_token = token
  current_user_profile.save()

  return HttpResponseRedirect('/wavesApp')

def spotify_login(request):
  current_user = request.user
  current_user_profile = UserProfile.objects.get(user=current_user)
  return HttpResponseRedirect('/wavesApp')

def current_user(request):
  current_user = request.user
  current_user_profile = UserProfile.objects.get(user=current_user)
  spotify_access_token = current_user_profile.spotify_access_token

  if spotify_access_token:
    sp = spotipy.Spotify(auth=spotify_access_token)

    current_spotify_user = sp.current_user()
    current_user_profile.spotify_id = current_spotify_user.id
    current_user_profile.spotify_external_urls = current_spotify_user.external_urls.spotify
    current_user_profile.spotify_followers =current_spotify_user.followers.total
  #   for item in results['items']:
  #       track = item['track']
  #       print(track['name'] + ' - ' + track['artists'][0]['name'])
  # UserProfile.current_user(current_user)
  return HttpResponseRedirect('/wavesApp')
  #UserProfile.get_liked_songs(current_user)



