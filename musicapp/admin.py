from django.contrib import admin
from .models import Artiste, Song, Lyric

# Register your models here.

django.admin.register(Artiste)
django.admin.register(Song)
django.admin.register(Lyric)
