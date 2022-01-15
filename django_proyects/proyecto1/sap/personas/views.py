from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render

from personas.models import Persona

# Create your views here.
def detalle_persona(request, id):
    # al utilizar la funcion get retorna un error si no existe el registro
    # persona_id = Persona.objects.get(pk=id)
    
    persona_id = get_object_or_404(Persona, pk=id)
    
    return render(request, 'detalle_persona.html', {'persona':persona_id})

# clase para generar el formulario con la informacion de a base de datos
PersonaForm = modelform_factory(Persona, exclude=[])

def nueva_persona(request):
    if request.method == 'POST':
        forma_persona = PersonaForm(request.POST)
        if forma_persona.is_valid():
            forma_persona.save()
            return redirect('index')
    else:
        forma_persona =PersonaForm()
    
    return render(request, 'nueva_persona.html', {'formaPersona':forma_persona})