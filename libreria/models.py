from django.db import models

class libro(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=200)

    def __str__(self):

        return f"Libro: {self.nombre} - Autor: {self.autor} - Categoria: {self.categoria}"

class pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    tematica = models.CharField(max_length=100)
    ano_estreno = models.IntegerField()

    def __str__(self):

        return f"Pelicula: {self.nombre} - Director: {self.director} - Categoria: {self.tematica} - Año {self.ano_estreno}"

class persona(models.Model):
    nombre = models.CharField(max_length=100)
    edad= models.IntegerField()
    email = models.EmailField()
    libros_preferidos = models.ForeignKey(libro, on_delete= models.CASCADE)
    peliculas_preferidas = models.ForeignKey(pelicula, on_delete= models.CASCADE)

    def __str__(self):

        return f"Nombre: {self.nombre} -Edad: {self.edad} - Libros: {self.libros_preferidos} - Peliculas: {self.peliculas_preferidas}"








