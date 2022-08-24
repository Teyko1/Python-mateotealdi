from unicodedata import name
from django.urls import path
from libreria.views import agregar_avatar, editar_usuario, registrar_usuario, LibrosDelete, LibrosUpdate, LibrosCreate, LibrosList, actualizar_pelicula, borrar_pelicula, busquedalibro, busquedapersona, iniciar_sesion, pelicula_preferida, principal, pelicula, crear_libro, busquedalibro, registrar_usuario, resultadolibro, busquedapersona, resultadopersona, peliculas
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("principal/", principal, name="principal"),
    path("peliculas/", peliculas, name ="peliculas"),
    path("libros/", LibrosList.as_view(), name ="libros"),
    path("crearlibro/", LibrosCreate.as_view(), name ="crearlibro"),
    path("libros/actualizar/<pk>",LibrosUpdate.as_view(), name="actualizarlibro"),
    path("libros/borrar/<pk>",LibrosDelete.as_view(), name="borrarlibro"),
    path("busquedalibro/", busquedalibro, name="busquedalibro"),
    path("resultadolibro/",resultadolibro, name="resultadolibro"),


    path("login/", iniciar_sesion, name="iniciar_sesion"),
    path("registrarse/", registrar_usuario, name="registrate"),
    path("logout/",LogoutView.as_view(template_name="libreria/logout.html"), name="logout"),
    path("editarusuario/", editar_usuario, name= "editarusuario"),
    path("agregaravatar", agregar_avatar, name="agregaravatar"),

    path("peliculas/borrar/<idpelicula>/", borrar_pelicula, name="borrarpelicula"),
    path("peliculas/editar/<id_pelicula>/", actualizar_pelicula, name="editarpelicula"),

    path("busquedapersona/", busquedapersona, name="busquedapersona"),
    path("resultadopersona/", resultadopersona, name ="resultadopersona"),
    path("resultadopersona/pelicula_preferida/", pelicula_preferida, name="pelicula_preferida"),
    
    
]
