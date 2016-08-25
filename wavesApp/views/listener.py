from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse

from django.template import loader

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def logout(request):
    logout(request)

def login(request):
  return render(request, 'wavesApp/login.html')

def create_user(request):
  print(request)
  context = {
    'username': '',
    'first_name': '',
    'last_name': '',
    'email': '',
    'password': '',
  }

  return render(request, 'wavesApp/register.html', context)


