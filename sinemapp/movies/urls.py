from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home_page"),
    path("theaters", views.theaters, name="movies_in_theaters"),
    path("upcoming", views.upcoming, name="upcoming_movies"),
    path("all", views.list_of_movies, name="list_of_movies"),
    path("<slug:slug>", views.movie_details, name="movie_details"),
    
]