from django.contrib import admin

from personas.models import Domicilio, Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Domicilio)