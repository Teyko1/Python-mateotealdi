from django.shortcuts import render, redirect
from django.http import HttpResponse
from libreria.models import persona, libro, pelicula
from libreria.forms import libroformulario, peliculaformulario,peliculafavorita

#Autentificacion
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


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

def peliculas(request):

    peliculas = pelicula.objects.all()

    context = {
        "mensaje": "Todos nuestros Libros!",
        "mensaje_bienvenida": "Bienvenid@s!",
        "peliculas": peliculas
    }
    return render(request, "libreria/peliculas.html", context)


def crear_pelicula(request):

    if request.method == "GET":
        formulario_pelicula = peliculaformulario()
        return render(request, "libreria/formulario.html", {"peliculafavorita": formulario_pelicula})
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


def busquedapersona(request):
    return render(request, "libreria/busquedapersona.html")

def resultadopersona(request):

    persona_nombre = request.GET.get("nombre", None)

    if not persona_nombre:
        return HttpResponse("No existe esa persona o no lo indicaste correctamente")
    
    else:

        persona_lista = persona.objects.all()

        return render(request, "libreria/resultadopersona.html", {"personas": persona_lista})


def pelicula_preferida(request):

    peliculas = peliculas.objects.all()

    if request.method == "GET":
        peliculafavorita = peliculafavorita()

        context = { "peliculafavorita" : peliculafavorita

        }
        return render(request, "libreria/formulario.html", context)
    else:
            peliculafavorita = peliculafavorita()
    
            peliculafavorita = persona(peliculafavorita = pelicula["nombre"])

            peliculafavorita.save() 
 
            return render(request, "libreria/resultadopersona/pelicula_preferida.html")
    

def iniciar_sesion(request):
    
    if request.method == "GET":
        formlogin = AuthenticationForm()

        context = { "formlogin" : formlogin

        }
    
        return render (request, "libreria/login.html", context)

    else:
        formlogin = AuthenticationForm(request, data=request.POST)

        if formlogin.is_valid():
            data = formlogin.cleaned_data

            usuario = authenticate(username=data.get("username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario),
                return redirect("principal")

            else:
                context = {

                    "error" : "Credenciales no validas",
                    "formlogin": formlogin
                }

                return render (request, "libreria/login.html", context)
      

    

    




