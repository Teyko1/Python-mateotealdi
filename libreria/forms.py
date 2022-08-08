from django.forms import Form, IntegerField, CharField

class libroformulario(Form):
    nombre = CharField(max_length=100)
    autor = CharField(max_length=100)
    categoria = CharField(max_length=200) 

class peliculaformulario(Form):
    nombre = CharField(max_length=100)
    director = CharField(max_length=100)
    tematica = CharField(max_length=100)
    ano_estreno = IntegerField()

class peliculafavorita(Form):
    peliculas_preferidas = CharField(max_length=100)

