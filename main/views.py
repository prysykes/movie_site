from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponse 
from .models import *
from .forms import AddMovieForm

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'main/index.html', context)
    
def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    context = {
            'movie': movie,
    }
    return render(request, 'main/details.html', context)

def add_movie(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('/')
    else:
        form = AddMovieForm()
    context = {
        'form': form,
        }

    return render(request, 'main/add_movie.html', context)

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
  
    if request.method == "POST":
        form = AddMovieForm(request.POST or None, instance=movie)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('details', movie_id)
    else:
        form = AddMovieForm(instance=movie)
    context = {
        'form': form
    }
    return render(request, 'main/add_movie.html', context)
