from django.shortcuts import render, redirect
from django.http import HttpResponse
from libreria.models import libro, pelicula, Avatar
from libreria.forms import libroformulario, peliculaformulario, Avatarform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Autentificacion
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from libreria.forms import creacionusuario, UserEditForm
from django.contrib.auth.models import User

#Mixing: permisos de usuario
from django.contrib.auth.mixins import LoginRequiredMixin

#Decoradores: permisos de usuario para funciones
from django.contrib.auth.decorators import login_required


@login_required
def principal(request):
    avatar = request.user.avatar.order_by('-pk').first()
    context = {}
    if avatar:
        context["imagen"] = avatar.imagen.url
    return render(request, "libreria/principal.html", context)


@login_required
def peliculas(request):
    
    peliculas = pelicula.objects.all()
    avatar = request.user.avatar.order_by('-pk').first()

    if request.method == "GET":
        formulario_pelicula = peliculaformulario()

        context = {
            "mensaje": "Todos nuestras Peliculas!",
            "mensaje_bienvenida": "Bienvenid@s!",
            "peliculas": peliculas,
            "formulario_pelicula": formulario_pelicula,
            "imagen": avatar.imagen.url
        }
        return render(request, "libreria/peliculas.html", context)

    else:
        formulario_pelicula = peliculaformulario(request.POST, request.FILES)
        if formulario_pelicula.is_valid():

            nombre = request.POST["nombre"]
            director = request.POST["director"]
            tematica = request.POST["tematica"] 
            ano_estreno = request.POST["ano_estreno"]
            tapa = request.FILES["tapa"]
            nueva_pelicula = pelicula(nombre = nombre, director = director, tematica = tematica, ano_estreno = ano_estreno, tapa = tapa)

            nueva_pelicula.save() 
            formulario_pelicula = peliculaformulario()

        context = {
            "mensaje": "Todos nuestras Peliculas!",
            "mensaje_bienvenida": "Bienvenid@s!",
            "peliculas": peliculas,
            "formulario_pelicula": formulario_pelicula
        }
 
        return render(request, "libreria/peliculas.html", context)

@login_required
def borrar_pelicula(request, idpelicula):

    try:
        movie = pelicula.objects.get(id=idpelicula)
        movie.delete()
        return redirect("peliculas")
    except:
        return HttpResponse(f"No se ha podido borrar la pelicula")


  
@login_required
def crear_libro(request):

    if request.method == "GET":
        formulario_libro = libroformulario()
        return render(request, "libreria/formlibro.html", {"formulario_libro":formulario_libro})
    else:

        formulario_libro = libroformulario(request.POST, request.FILES)

    if formulario_libro.is_valid():
   
    
        nombre = request.POST["nombre"]
        autor = request.POST["autor"]
        categoria = request.POST["categoria"]
        tapa = request.FILES["tapa"]

        nuevo_libro = libro(nombre = nombre, autor = autor, categoria = categoria, tapa = tapa)

        nuevo_libro.save() 
 
        return render(request, "libreria/principal.html", {"formulario_libro":formulario_libro})

    else:
        return HttpResponse("Formulario no valido")


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

                context= {
                    "error": "Credenciales no validas",
                    "formlogin": formlogin
                    }
             
                return render (request, "libreria/login.html", context)
        else:

            context= {
                    "error": "Formulario no valido",
                    "formlogin": formlogin
                    }
             
            return render (request, "libreria/login.html", context)

def registrar_usuario(request):
    if request.method == "GET":
        formulario = creacionusuario()
        return render(request, "libreria/registro.html", {"formulario": formulario}) 

    else:
        formulario = creacionusuario(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect("principal")
        else:
            return render(request, "libreria/registro.html", {"formulario": formulario,"error":"Formulario no valido"})

def sobremi(request):
    avatar = request.user.avatar.order_by('-pk').first()
    context = {}
    if avatar:
        context["imagen"] = avatar.imagen.url

    return render(request, "libreria/sobremi.html", context)



class LibrosList(LoginRequiredMixin, ListView):
    model = libro
    template_name = "libreria/libros_list.html"
    


class LibrosCreate(LoginRequiredMixin, CreateView):
    model = libro
    success_url = "/libreria/libros/"
    fields = ["nombre", "autor", "categoria", "tapa"]


class LibrosUpdate(LoginRequiredMixin, UpdateView):
    model = libro
    success_url = "/libreria/libros/"
    fields = ["nombre", "autor", "categoria", "tapa"]


class PeliculasUpdate(LoginRequiredMixin, UpdateView):
    model = pelicula
    success_url = "/libreria/peliculas/"
    fields = ["nombre", "director", "tematica","ano_estreno", "tapa"]

class LibrosDelete(LoginRequiredMixin, DeleteView):
    model = libro
    success_url = "/libreria/libros/"



@login_required
def editar_usuario(request):
    if request.method == "GET":
        form = UserEditForm(initial={"username": request.user.username, "first_name": request.user.first_name, "last_name": request.user.last_name})
        return render(request, "libreria/editarusuario.html", {"form": form})

    else:
        form= UserEditForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data

            usuario = request.user
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]


            usuario.save()

            return redirect("principal")

    return render(request, "libreria/editarusuario.html", {"form": form})

@login_required
def agregar_avatar(request):
    if request.method == "GET":
        form = Avatarform()
        context = {"form": form}
        return render(request, "libreria/agregar_avatar.html", context)

    else:
        form = Avatarform(request.POST, request.FILES)

        if form.is_valid():
            data= form.cleaned_data
            avatar = Avatar(user=request.user, imagen= data["imagen"])
            avatar.save()

        return render(request, "libreria/principal.html")
        





