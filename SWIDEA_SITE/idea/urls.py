from django.urls import path
from . import views

app_name = "idea"

urlpatterns = [
    path("", views.idea_list, name="list"),
    path("create/", views.idea_create, name="create"),
    path("<int:idea_id>/", views.idea_detail, name="detail"),
    path("<int:idea_id>/update/", views.idea_update, name="update"),
    path("<int:idea_id>/delete/", views.idea_delete, name="delete"),
    
    path("interest/<int:idea_id>/<str:direction>/", views.update_interest, name="update_interest"),
    path("star/<int:idea_id>/", views.toggle_star, name="toggle_star"),
]