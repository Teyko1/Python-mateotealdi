from django.shortcuts import render
from django.http import HttpResponse
from libreria.models import persona, libro, pelicula
from libreria.forms import libroformulario, peliculaformulario


def principal(request):
    return render(request, "libreria/principal.html")

def libros(request):

    libros = libro.objects.all()

    context = {
        "mensaje": "Todos nuestros Libros!",
        "mensaje_bienvenida": "Bienvenid@s!",
        "libros": libros
    }
    return render(request, "libreria/libros.html", context)


def crear_pelicula(request):

    if request.method == "GET":
        formulario_pelicula = peliculaformulario()
        return render(request, "libreria/formulario.html", {"formulario_pelicula": formulario_pelicula})
    else:
        nombre = request.POST["nombre"]
        director = request.POST["director"]
        tematica = request.POST["tematica"] 
        ano_estreno = request.POST["ano_estreno"]
        nueva_pelicula = pelicula(nombre = nombre, director = director, tematica = tematica, ano_estreno = ano_estreno)

        nueva_pelicula.save() 
 
        return render(request, "libreria/principal.html")

def crear_libro(request):

    if request.method == "GET":
        formulario = libroformulario()
        return render(request, "libreria/formlibro.html", {"formulario_libro":formulario})
    else:

        formulario = libroformulario(request.POST)

    if formulario.is_valid():
        data = formulario.cleaned_data
        print(data)


        nombre = data["nombre"]
        autor = data["autor"]
        categoria = data["categoria"] 
        
        nuevo_libro = libro(nombre = nombre, autor = autor, categoria = categoria)

        nuevo_libro.save() 
 
        return render(request, "libreria/principal.html")

    else:
        return HttpResponse("Formulario no valido")


def busquedalibro(request):
    return render(request, "libreria/busquedalibro.html")

def resultadolibro(request):

    libro_nombre = request.GET.get("Libro", None)

    if not libro_nombre:
        return HttpResponse("No existe ese libro o no lo indicaste correctamente")
    
    else:

        libros_lista = libro.objects.filter(nombre__icontains=libro_nombre)

        return render(request, "libreria/resultadolibro.html", {"libros": libros_lista})

    




    

    




