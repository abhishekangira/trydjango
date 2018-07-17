from django.shortcuts import render
from .models import Song
# Create your views here.
def song_detail_view(request):
    item = Song.objects.get(id=1)
    context = {
    'user':request.user,
    'song': item
    }
    return render(request, 'songs/detail.html', context)
