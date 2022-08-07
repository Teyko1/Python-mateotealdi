from django.urls import path
from libreria.views import formulario, principal, pelicula, formulario, crear_pelicula

urlpatterns = [
    path("principal/", principal, name="principal"),
    path("pelicula/", pelicula, name ="pelicula"),
    path("formulario/", formulario, name ="formulario"),
    path("pelicula/crear/", crear_pelicula, name ="crearpelicula"),
    
    
]
