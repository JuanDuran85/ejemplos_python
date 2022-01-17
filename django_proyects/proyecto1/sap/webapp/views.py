from django.http.response import HttpResponse
from django.shortcuts import render

from personas.models import Persona

# Create your views here.

def bienvenidos(request):
    # se utiliza las clases del modelo para trear los objetos
    numero_personas = Persona.objects.count()
    # el all trae todos los campos sin orden
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id','nombre')
    return render(request, 'bienvenido.html', {'numero_personas':numero_personas, 'personas':personas})