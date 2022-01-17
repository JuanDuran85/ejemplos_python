
from attr import attrs
from django.forms import EmailInput, ModelForm

from personas.models import Persona


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),
        }