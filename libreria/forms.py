from re import I
from tkinter import Label, Widget
from django.forms import Form, IntegerField, CharField, EmailField, PasswordInput, ImageField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import libro, pelicula
from django import forms

class libroformulario(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['nombre', 'autor', 'categoria',  'tapa']

class peliculaformulario(forms.ModelForm):

    class Meta:
        model = pelicula
        fields = ['nombre', 'director', 'tematica', 'ano_estreno', 'tapa']



class Avatarform(Form):
    imagen= ImageField()


class creacionusuario(UserCreationForm):
    username = CharField(label= "Usuario")
    email = EmailField()
    password1 = CharField(label= "Contraseña", widget=PasswordInput)
    password2 = CharField(label= "Confirmar contraseña", widget=PasswordInput)
    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email = EmailField(label="Modificar E-mail")
    password1 = CharField(label= "Modificar contraseña", widget=PasswordInput)
    password2 = CharField(label= "Confirmar contraseña nueva", widget=PasswordInput)
    last_name = CharField(label= "Apellido")
    first_name = CharField(label= "Nombre")

    class Meta:
        model = User
        fields = ["last_name", "first_name" ,"email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


