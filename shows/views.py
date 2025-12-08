from django.shortcuts import render
from . import models

# Create your views here.
def show_list(request):
    shows = models.Show.objects.all()
    return render(request, 'shows/shows.html', {'shows': shows})