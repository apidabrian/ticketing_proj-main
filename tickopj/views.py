from django.shortcuts import render
from movies.models import Movie
from shows.models import LiveShow
from events.models import Event
from shows.models import Shows
from events.models import Event
from movies.models import Movie
from liveshows.models import LiveShows
from django.db.models import Q


def home(request):
    current_movies = Movie.objects.filter(is_current=True)
    live_shows = LiveShow.objects.all()
    events = Event.objects.all()

    context = {
        'current_movies': current_movies,
        'live_shows': live_shows,
        'events': events,
    }
    return render(request, 'home.html', context)

def search_view(request):
    query = request.GET.get("q", "")

    movies = Movie.objects.filter(
        Q(title__icontains=query) | 
        Q(description__icontains=query)
    )

    events = Event.objects.filter(
        Q(title__icontains=query) | 
        Q(description__icontains=query)
    )

    liveshows = LiveShow.objects.filter(
        Q(title__icontains=query) | 
        Q(description__icontains=query)
    )
    
    shows = Shows.objects.filter(
        Q(title__icontains=query) | 
        Q(description__icontains=query)
    )

    context = {
        "query": query,
        "movies": movies,
        "events": events,
        "liveshows": liveshows,
        "shows": shows,
    }
    return render(request, "search_results.html", context)


def about(request):
    return render(request, 'about.html') 

def privacy_policy(request):
    return render(request, 'privacy_policy.html')   

def terms(request):
    return render(request, 'terms.html')

def help(request):
    return render(request, 'help.html')

def contacts(request):
    return render(request, 'contacts/contact.html')

def show_list(request):
    return render(request, 'shows/shows.html')

def event_list(request):
    return render(request, 'events/events.html')

def movie_list(request):
    return render(request, 'movies/movies.html')    

def live_show_list(request):
    return render(request, 'liveshows/liveshows.html')
    