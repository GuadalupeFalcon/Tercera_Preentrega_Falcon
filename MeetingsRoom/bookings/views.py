from django.shortcuts import render

from django.http import HttpResponse



def home_view(request):
    return HttpResponse("<h1>Bienvenidos a la Aplicacion de Reservas.</h1> <h2> Reserva tu sala!!!</h2>")

def list_view(request):
    contexto_dict = {
        'reservas': [
            {"usuario": "Emiliano Martínez ", "sala": "arquero"},
            {"usuario": "Nicolas Otamendi ", "sala": "defensor"},
            {"usuario": "Nahuel Molina ", "sala": "defensor"},
            {"usuario": "Gonzalo Montiel ", "sala": "defensor"},
            {"usuario": "Lisando Martinez ", "sala": "defensor"},
            {"usuario": "Angel di maria", "sala": "mediocampista"},
            {"usuario": "Julián Álvarez", "sala": "delantero"},
        ]
    }
    return render(request, "bookings/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    return HttpResponse(f"<h1>Estas buscnado las reservas de {nombre_de_usuario} </h1>")
    #reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    #contexto_dict = {"reservas": reservas_del_usuario}
    #return render(request, "bookings/list.html", contexto_dict)