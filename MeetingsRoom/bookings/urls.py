
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def mi_view(request):
    return HttpResponse("<h1>Bienvenidos a la Aplicacion de Reserva de Salas!</h1>")


urlpatterns = [
    path("", mi_view),
]