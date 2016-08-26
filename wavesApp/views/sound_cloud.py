from django.shortcuts               import render_to_response
from django.http                    import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers       import reverse
from django.conf                    import settings
from django.contrib.auth            import login, logout, authenticate
from django.template                import Context, loader
from django.core.cache              import cache

import urllib, cgi, simplejson
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



