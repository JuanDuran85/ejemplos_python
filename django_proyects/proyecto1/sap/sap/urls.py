from django.contrib import admin
from django.urls import path
from personas.views import detalle_persona, editar_persona, eliminar_persona, nueva_persona

from webapp.views import bienvenidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos, name='index'),
    path('detalle_persona/<int:id>', detalle_persona),
    path('nueva_persona', nueva_persona),
    path('editar_persona/<int:id>', editar_persona),
    path('eliminar_persona/<int:id>', eliminar_persona),
]
