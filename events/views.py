from django.shortcuts import render
from . import models

# Create your views here.
def event_list(request):
    events = models.Event.objects.all()
    return render(request, 'events/events.html', {'events': events})