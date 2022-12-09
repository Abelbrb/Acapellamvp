from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Room,Song,Playlist


def create(request):
    if request.method == 'POST':
        title=request.POST['title']
        url=request.POST['url']
        rom=request.POST['room']
        r=Room.objects.get(slug=rom)
        new_song = Song(song_name=title,songurl=url)
        new_song.save()
        success='Song Created in'+ rom
        if Playlist.objects.filter(room=r).exists():
            p = Playlist.objects.get(room=r)
            p.song.add(new_song)
        else:
            p = Playlist(list_name=rom,room=r,song=new_song)
            p.save()     
        return HttpResponse(success)

        

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)

    return render(request, 'room/room.html', {'room': room})
