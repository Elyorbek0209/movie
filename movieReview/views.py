from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # Key & Value Pair with Dictionary
    all_movies = MovieInfo.objects.all()
    context = {'Movies': all_movies}    

    context = {'MovieName': ['Titanik', 'Braveheart', 'Pursue of Success']}    

    return render(request, 'movieReview/index.html', context)


def addMovie(request):
    return render(request, 'movieReview/add_movie.html')
