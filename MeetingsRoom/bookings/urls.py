
from django.contrib import admin
from django.urls import path
from .views import home_view , list_view , search_view , create_view

urlpatterns = [
    path("", home_view),
    path("list/", list_view, name="bookings-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("crear/<nombre_de_usuario>/<sala>", create_view),
]