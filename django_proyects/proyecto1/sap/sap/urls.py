from django.contrib import admin
from django.urls import path
from personas.views import detalle_persona, nueva_persona

from webapp.views import bienvenidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos, name='index'),
    path('detalle_persona/<int:id>', detalle_persona),
    path('nueva_persona', nueva_persona),
]
