from django.http import HttpResponse
from django.template import Template, Context


def index(request):
    archivo = open(r"C:\Python 3.10\proyecto_libreria\proyecto_libreria\templates\index.html", "r")
    contenido_html = archivo.read()
    archivo.close()
    plantilla = Template(contenido_html)
    contexto = Context()
    documento_renderizado = plantilla.render(contexto)
    return HttpResponse(documento_renderizado)
