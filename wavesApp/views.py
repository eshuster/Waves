from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Song

def index(request):
  latest_song_list = Song.objects.order_by('-date_added')[:5]
  template = loader.get_template('wavesApp/index.html')
  context = {
      'latest_song_list': latest_song_list,
    }
  # return HttpResponse(template.render(context, request))
  return render(request, 'wavesApp/index.html', context)

def detail(request, song_id):
  try:
    song = get_object_or_404(Song, pk=song_id)
  except song.DoesNotExist:
    raise Http404("song does not exist")
  return render(request, 'wavesApp/detail.html', {'song': song})

def results(request, song_id):
  response = "You're looking at the results of song %s."
  return HttpResponse(response % song_id)

def vote(request, song_id):
  return HttpResponse("You're voting on song %s." % song_id)
