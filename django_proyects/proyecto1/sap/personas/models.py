from django.db import models

# Create your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}-{self.calle} {self.numero} {self.pais}'

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.id}-{self.nombre} {self.apellido}'