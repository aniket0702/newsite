# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length=100)
    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album,on_delete= models.CASCADE)
    song_name = models.CharField(max_length = 100)
    fav = models.IntegerField(default = 0)
    def __str__(self):
        return str(self.album.id) + ". " + self.song_name
