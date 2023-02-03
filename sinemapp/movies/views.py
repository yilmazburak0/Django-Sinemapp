from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import CommentForm
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.contrib import messages



def index(request):
    released_movies = Movie.objects.filter(is_released=True)
    return render(request,"home-page.html",{
        'movies':released_movies,
    })

@login_required(login_url="/account/login")
def theaters(request):   
    released_movies = Movie.objects.filter(is_released=True)
    return render(request,"theaters.html",{
        'movies':released_movies,
    })

@login_required(login_url="/account/login")
def upcoming(request):
    coming_movies = Movie.objects.filter(is_coming=True)
    return render(request,"upcoming.html",{
        'coming_movies': coming_movies,
    })


def movie_details(request,slug):
    movie = get_object_or_404(Movie, slug=slug)
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # save edilecek objeyi veri tabanına göndermeden önce değişiklik yapıp gönderiyoruz.
            comment= comment_form.save(commit=False)
            comment.movie = movie
            comment.save()
            messages.info(request,"yorumunuz kaydedildi")
            return HttpResponseRedirect(reverse("movie_details",args=[slug]))

    videos = movie.video_set.all()
    print(videos)
    
    return render(request,"movie-details.html",{
        'movie':movie,
        'genres':movie.genres.all(),
        'people':movie.people.all(),
        "videos": movie.video_set.all(),
        "comments":movie.comments.all().order_by("-date_added"),
        "comment_form": comment_form
    })


@login_required(login_url="/account/login")
def list_of_movies(request):
    if 'q' in request.GET and request.GET.get('q'):
        movie_name = request.GET['q']
        movies = Movie.objects.filter(title__contains=movie_name)
        if len(movies)==0:
            return render(request, 'unsuccessful.html',{
                "searced_word":movie_name,
            })

    else:
        movies = Movie.objects.all()  

    context = {
        "movies": movies,
    }

    return render(request, 'list_of_movies.html', context)