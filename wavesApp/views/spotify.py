from django.http                    import HttpResponseRedirect, HttpResponse
from django.conf                    import settings

import urllib, cgi, simplejson
import spotipy, sys
import spotipy.util as util


def to_spotify_login(request):
  global scope
  scope = 'user-library'

  if len(sys.argv) > 1:
    global username
    username = sys.argv[1]
  else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

  global token
  token = util.prompt_for_user_token(username, scope,
                        client_id=settings.SPOTIFY_CLIENT_ID,
                        client_secret=settings.SPOTIFY_CLIENT_SECRET,
                        redirect_uri='http://127.0.0.1:8000/wavesApp/')
  return HttpResponseRedirect('/wavesApp/')


def spotify_login(request):
  username = sys.argv[1]
  return username


def get_liked_songs(request):
  if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
  return HttpResponseRedirect('/wavesApp')



