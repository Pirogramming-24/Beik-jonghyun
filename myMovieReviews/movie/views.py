from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == "POST":
        Movie.objects.create(
            title=request.POST['title'],
            year = request.POST['year'],
            director=request.POST['director'],
            actor=request.POST['actor'],
            genre=request.POST['genre'],
            rating=request.POST['rating'],
            runtime=request.POST['runtime'],
            content=request.POST['content'],
        )
        return redirect('movie:list')
    return render(request, 'movie/movie_form.html')

def movie_update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == "POST":
        movie.title = request.POST['title']
        movie.year = request.POST['year']
        movie.director = request.POST['director']
        movie.actor = request.POST['actor']
        movie.genre = request.POST['genre']
        movie.rating = request.POST['rating']
        movie.runtime = request.POST['runtime']
        movie.content = request.POST['content']
        movie.save()
        return redirect('movie:detail', movie_id=movie.id)
    return render(request, 'movie/movie_form.html', {'movie': movie})

def movie_delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect('movie:list')
