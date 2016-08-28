from django.http                    import HttpResponseRedirect, HttpResponse
from django.conf                    import settings

import soundcloud




def sc_login(request):
    client = soundcloud.Client(client_id=settings.SC_CONSUMER, client_secret=settings.SC_CONSUMER_SECRET, redirect_uri=settings.SC_CALLBACK_HOST + 'sc_login/')
    code = request.GET['code']
    access_token = client.exchange_token(code)
    return HttpResponseRedirect('/wavesApp')

def to_sc_login(request):
    client = soundcloud.Client(client_id=settings.SC_CONSUMER,
                           client_secret=settings.SC_CONSUMER_SECRET,
                           redirect_uri=settings.SC_CALLBACK_HOST + 'sc_login/')
    return HttpResponseRedirect(client.authorize_url())



