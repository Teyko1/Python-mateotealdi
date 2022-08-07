from django.shortcuts import render
from django.http import HttpResponse
from libreria.models import persona, libro, pelicula


def principal(request):
    return render(request, "libreria/principal.html")

def pelicula(request):
    return render(request, "libreria/pelicula.html")


def crear_pelicula(request):

    if request.method == "GET":
        return render(request, "libreria/formulario.html")
    else:
        nombre = request.POST["nombre"]
        director = request.POST["director"]
        tematica = request.POST["tematica"] 
        ano_estreno = request.POST["ano_estreno"]
        nueva_pelicula = pelicula(nombre = nombre, director = director, tematica = tematica, ano_estreno = ano_estreno)

        nueva_pelicula.save() 
 
        return render(request, "libreria/principal.html")




