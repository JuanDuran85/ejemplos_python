from django.contrib import admin
from django.urls import path
from personas.views import detalle_persona

from webapp.views import bienvenidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos),
    path('detalle_persona/<int:id>', detalle_persona),
]
