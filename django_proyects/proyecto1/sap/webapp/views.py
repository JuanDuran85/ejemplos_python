from django.http.response import HttpResponse
from django.shortcuts import render

from personas.models import Persona

# Create your views here.

def bienvenidos(request):
    # se utiliza las clases del modelo para trear los objetos
    numero_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {'numero_personas':numero_personas, 'personas':personas})