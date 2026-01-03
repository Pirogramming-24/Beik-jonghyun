from django.urls import path
from . import views

app_name = "devtools"

urlpatterns = [
    path("", views.devtool_list, name = "list"),
    path("create/", views.devtool_create, name = "create"),
    path("<int:devtool_id>/", views.devtool_detail, name = "detail"),
    path("<int:devtool_id>/update/", views.devtool_update, name = "update"),
    path("<int:devtool_id>/delete/", views.devtool_delete, name = "delete"),
]