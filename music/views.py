# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,reverse
from .models import Album,Song
# Create your views here.
def index(request):
    html = ""
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request,'music/index.html',context)


def detail(request,album_id):
    album = get_object_or_404(Album,pk = album_id)
    s = album.song_set.all().order_by("-fav")
    context = {'songs':s,'album':album}
    return render(request,'music/detail.html',context)


def favourite(request,album_id):
    album = get_object_or_404(Album,pk = album_id)
    try:
        sel_song = album.song_set.get(pk = request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{'album':album,'error_message':"Song Does not exist"})
    else:
        sel_song.fav += 1
        sel_song.save()
        return HttpResponseRedirect(reverse('music:detail', args=(album.id,)))
