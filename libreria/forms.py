from tkinter import Widget
from django.forms import Form, IntegerField, CharField, EmailField, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class creacionusuario(UserCreationForm):
    username = CharField(label= "Usuario")
    email = EmailField()
    password1 = CharField(label= "Contraseña", widget=PasswordInput)
    password2 = CharField(label= "Confirmar contraseña", widget=PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


