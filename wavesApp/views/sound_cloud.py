from django.http                    import HttpResponseRedirect, HttpResponse
from django.conf                    import settings

import soundcloud

from django.forms.models import model_to_dict
from wavesApp.models.user_profile import UserProfile




def sc_login(request):
  current_user = request.user
  current_user_profile = UserProfile.objects.get(user=current_user)
  client = soundcloud.Client(client_id=settings.SC_CONSUMER, client_secret=settings.SC_CONSUMER_SECRET, redirect_uri=settings.SC_CALLBACK_HOST + 'sc_login/')
  code = request.GET['code']
  access_token = client.exchange_token(code)
  current_user_profile.soundcloud_access_token = access_token.fields()['access_token']
  current_user_profile.save()
  return HttpResponseRedirect('/wavesApp')

def to_sc_login(request):
    client = soundcloud.Client(client_id=settings.SC_CONSUMER,
                           client_secret=settings.SC_CONSUMER_SECRET,
                           redirect_uri=settings.SC_CALLBACK_HOST + 'sc_login/')
    return HttpResponseRedirect(client.authorize_url())



