from django.urls import path
from libreria.views import principal, pelicula, crear_pelicula

urlpatterns = [
    path("principal/", principal, name="principal"),
    path("pelicula/", pelicula, name ="pelicula"),
    path("crearpelicula/", crear_pelicula, name ="crearpelicula"),
    
    
]
