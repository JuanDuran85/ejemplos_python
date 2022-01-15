from django.shortcuts import render

from personas.models import Persona

# Create your views here.
def detalle_persona(request, id):
    persona_id = Persona.objects.get(pk=id)
    return render(request, 'detalle_persona.html', {'persona':persona_id})