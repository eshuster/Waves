from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from wavesApp.models.user_profile import UserProfile

def index(request):

  current_user = request.user
  current_user_profile = UserProfile.objects.get(user=current_user)

  context = {
        'sc_url': '<h1 class="login-to-soundcloud"><a href="to_sc_login">Connect to Soundcloud</a></h1>',
        'spotify_url': '<h1 class="login-to-spotify"><a href="to_spotify_login">Connect to Spotify</a></h1>',
        'current_user_profile_sc_access_token': current_user_profile.soundcloud_access_token,
         'current_user_profile_spotify_access_token': current_user_profile.spotify_access_token
        }

  return render(request, 'wavesApp/index.html', context)

def detail(request, song_id):
  template = loader.get_template('wavesApp/detail.html')
  try:
    song = get_object_or_404(Song, pk=song_id)
  except song.DoesNotExist:
    raise Http404("song does not exist")
  return render(request, 'wavesApp/detail.html', {'song': song})
