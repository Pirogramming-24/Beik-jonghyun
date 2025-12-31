from django.urls import path
from . import views

app_name = "movie"

urlpatterns = [
    path("", views.movie_list, name="list"),
    path("create/", views.movie_create, name="create"),
    path("<int:movie_id>/", views.movie_detail, name="detail"),
    path("<int:movie_id>/update/", views.movie_update, name="update"),
    path("<int:movie_id>/delete/", views.movie_delete, name="delete"),
]