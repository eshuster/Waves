from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

def index(request):
  context = {
      'latest_song_list': "nada",
    }
  return render(request, 'wavesApp/index.html', context)

def detail(request, song_id):
  template = loader.get_template('wavesApp/detail.html')
  try:
    song = get_object_or_404(Song, pk=song_id)
  except song.DoesNotExist:
    raise Http404("song does not exist")
  return render(request, 'wavesApp/detail.html', {'song': song})
