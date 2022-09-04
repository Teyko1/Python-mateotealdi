from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=200)
    tapa = models.ImageField(upload_to= 'media/', null= True)

    def __str__(self):

        return f"Libro: {self.nombre} - Autor: {self.autor} - Categoria: {self.categoria} - Tapa: {self.tapa}"

class pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    tematica = models.CharField(max_length=100)
    ano_estreno = models.IntegerField()
    tapa = models.ImageField(upload_to= 'media/', null= True)

    def __str__(self):

        return f"Pelicula: {self.nombre} - Director: {self.director} - Categoria: {self.tematica} - Año {self.ano_estreno} - Tapa: {self.tapa}"


class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'avatar')
    #Subcarpeta de avatares
    imagen = models.ImageField(upload_to= "avatares", null= True, blank= True)

