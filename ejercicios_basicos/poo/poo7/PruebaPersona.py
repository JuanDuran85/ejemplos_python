# con asterisco * se importa todas las clases del archivo

from Personas import Persona

print("Creando Objetos".center(50, "-"))
persona1 = Persona("Juan", "Perez", 23)
persona2 = Persona("Pedro", "Gomez", 33)

persona1.mostrar_detalles()
persona2.mostrar_detalles()

print("Eliminando Objetos".center(50, "-"))
del persona2

