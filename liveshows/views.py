from django.shortcuts import render
from . import models    

# Create your views here.
def live_show_list(request):
    live_shows = models.LiveShow.objects.all()
    return render(request, 'liveshows/liveshows.html', {'live_shows': live_shows})