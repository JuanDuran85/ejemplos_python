# trabajando con POO en python

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'La persona es: Nombre: {self.nombre}, Apellido: {self.apellido} y Edad: {self.edad}')

persona1 = Persona('Juan', 'Perez', 30)
persona1.mostrar_detalle()
# crear nuevo atributo para la clase persona
persona1.altura = 180
print(persona1.altura)

persona2 = Persona('Pedro', 'Gomez', 40)
persona2.mostrar_detalle()

# otra manera de llamar un metodo es (no es común):
Persona.mostrar_detalle(persona1)
