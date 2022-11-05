from django.db import models

# Create your models here.

class Artiste(models.Model):
  first_name = models.Charfield(max_length=40)
  last_name = models.Charfield(max_length=40)
  age = models.IntegerField()

class Song(models.Model):
  title = models.Charfield(max_length=50)
  date_released = models.DateField()
  likes = models.IntegerField()
  artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
  content = models.CharField(max_length=400)
  song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
