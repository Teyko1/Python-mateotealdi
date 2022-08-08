from django.urls import path
from libreria.views import busquedalibro, busquedapersona, principal, pelicula, crear_pelicula, crear_libro, libros, busquedalibro, resultadolibro, busquedapersona, resultadopersona

urlpatterns = [
    path("principal/", principal, name="principal"),
    path("libros/", libros, name ="libros"),
    path("crearpelicula/", crear_pelicula, name ="crearpelicula"),
    path("crearlibro/", crear_libro, name ="crearlibro"),
    path("busquedalibro/", busquedalibro, name="busquedalibro"),
    path("resultadolibro/",resultadolibro, name="resultadolibro"),
    path("busquedapersona/", busquedapersona, name="busquedapersona"),
    path("resultadopersona/", resultadopersona, name ="resultadopersona")

    
    
]
