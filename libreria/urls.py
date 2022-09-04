from unicodedata import name
from django.urls import path
from libreria.views import PeliculasUpdate, sobremi, agregar_avatar, editar_usuario, registrar_usuario, LibrosDelete, LibrosUpdate, LibrosCreate, LibrosList, borrar_pelicula, iniciar_sesion, principal, pelicula, registrar_usuario, peliculas
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("principal/", principal, name="principal"),
    path("peliculas/", peliculas, name ="peliculas"),
    path("libros/", LibrosList.as_view(), name ="libros"),
    path("libroscompleto/", LibrosList.as_view(), name ="libroscompleto"),
    path("crearlibro/", LibrosCreate.as_view() , name ="crearlibro"),
    path("libros/actualizar/<pk>",LibrosUpdate.as_view(), name="actualizarlibro"),
    path("libros/borrar/<pk>",LibrosDelete.as_view(), name="borrarlibro"),


    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("registrarse/", registrar_usuario, name="registrate"),
    path("logout/",LogoutView.as_view(template_name="libreria/logout.html"), name="logout"),
    path("editarusuario/", editar_usuario, name= "editarusuario"),
    path("agregaravatar", agregar_avatar, name="agregaravatar"),
    path("sobremi", sobremi, name="sobremi"),

    path("peliculas/borrar/<idpelicula>/", borrar_pelicula, name="borrarpelicula"),
    path("peliculas/editar/<pk>/", PeliculasUpdate.as_view(), name="editarpelicula"),

    
    
]
