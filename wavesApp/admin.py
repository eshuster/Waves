from django.contrib import admin
# Register your models here.

from .models.user_profile import UserProfile
from .models.genre import Genre
from .models.song import Song
from .models.playlist import Playlist
from .models.listener import Listener


admin.site.register(UserProfile)
admin.site.register(Genre)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Listener)

