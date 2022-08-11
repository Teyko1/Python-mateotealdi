from django.urls import path
from libreria.views import busquedalibro, busquedapersona, iniciar_sesion, pelicula_preferida, principal, pelicula, crear_pelicula, crear_libro, libros, busquedalibro, resultadolibro, busquedapersona, resultadopersona, peliculas

urlpatterns = [
    path("principal/", principal, name="principal"),
    path("peliculas/", peliculas, name ="peliculas"),
    path("libros/", libros, name ="libros"),
    path("crearpelicula/", crear_pelicula, name ="crearpelicula"),
    path("crearlibro/", crear_libro, name ="crearlibro"),
    path("busquedalibro/", busquedalibro, name="busquedalibro"),
    path("resultadolibro/",resultadolibro, name="resultadolibro"),
    path("busquedapersona/", busquedapersona, name="busquedapersona"),
    path("resultadopersona/", resultadopersona, name ="resultadopersona"),
    path("resultadopersona/pelicula_preferida/", pelicula_preferida, name="pelicula_preferida"),
    path("login/", iniciar_sesion, name="iniciar_sesion"),


    
    
]
