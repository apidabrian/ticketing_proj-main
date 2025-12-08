from django.shortcuts import render, get_object_or_404
from . import models

# Movie list page
def movie_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': movies})

# Movie detail page
def movie_detail(request, movie_id):
    movie = get_object_or_404(models.Movie, id=movie_id)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
