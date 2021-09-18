# trabajando con POO en python

class Persona:
    # si se quiere pasar una tupla de valores se usa el *args
    # si se quiere pasar una lista de valores se usa el **kwargs
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La persona es: Nombre: {self.nombre}, Apellido: {self.apellido} y Edad: {self.edad}, tupla de valores: {self.args}. Diccionario de datos: {self.kwargs}')

persona1 = Persona('Juan', 'Perez', 30, '3343344', 3, 4,5, m='Manzana', p='Pera', a='Aguacate')
persona1.mostrar_detalle()
# crear nuevo atributo para la clase persona
persona1.altura = 180
print(persona1.altura)

persona2 = Persona('Pedro', 'Gomez', 40)
persona2.mostrar_detalle()

# otra manera de llamar un metodo es (no es común):
Persona.mostrar_detalle(persona1)
