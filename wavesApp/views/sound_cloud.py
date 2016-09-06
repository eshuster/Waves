from django.http                    import HttpResponseRedirect, HttpResponse
from django.conf                    import settings
from django.forms.models            import model_to_dict
from wavesApp.models.user_profile   import UserProfile

import soundcloud

def sc_login(request):
  current_user = request.user
  current_user_profile = UserProfile.objects.get(user=current_user)

  code = request.GET['code']
  access_token = client.exchange_token(code)
  print()
  print()
  print(access_token.keys())
  print(access_token.obj['access_token'])
  print()
  print()
  current_user_profile.soundcloud_access_token = access_token.obj['access_token']
  current_user_profile.save()

  tracks = client.get('/tracks', q='buskers', license='cc-by-sa')
  me = client.get('/me').username

  print(me)
  return HttpResponseRedirect('/wavesApp')

def to_sc_login(request):
  global client
  client = soundcloud.Client(client_id=settings.SC_CONSUMER,
                           client_secret=settings.SC_CONSUMER_SECRET,
                           redirect_uri=settings.SC_CALLBACK_HOST + 'sc_login')
  print(client.authorize_url())
  return HttpResponseRedirect(client.authorize_url())

def user_info(request):
  # Move to model soon
  current_user = request.user
  current_user_profile = UserProfile.objects.get(user=current_user)

  client = soundcloud.Client(access_token=current_user_profile.soundcloud_access_token)

  user = client.get('/me')

  current_user_profile.soundcloud_user_id = user.id
  current_user_profile.soundcloud_username = user.username
  current_user_profile.soundcloud_user_track_count = user.track_count
  current_user_profile.soundcloud_user_playlist_count = user.playlist_count
  current_user_profile.soundcloud_user_public_favorites_count = user.public_favorites_count
  current_user_profile.soundcloud_user_private_tracks_count = user.private_tracks_count
  current_user_profile.soundcloud_user_private_playlists_count = user.private_playlists_count

  current_user_profile.save()

  return HttpResponseRedirect('/wavesApp')



