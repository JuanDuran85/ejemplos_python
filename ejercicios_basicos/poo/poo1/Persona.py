# trabajando con clases (POO)

class Ejemplo:
    pass  # la clase no tendra contenido, solo se utiliza para definir una clase


print(type(Ejemplo))


class Persona:
    # self es una referencia al objeto que se esta creando
    # el __ al inicio y al final se le conoce como metodo 'dunder' = 'double underscore'
    def __init__(self, nombre, edad):
        # estos son los atributos de la instancia
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Hola, soy una persona, mi nombre es: ", self.nombre, "y mi edad: ", self.edad)


persona_uno = Persona("Juan", 36)
print(persona_uno.nombre)
print(persona_uno.edad)
persona_uno.imprimir()


class Automovil:
    # Recuerde programar el constructor de clase que inicializa los 3 atributos
    def __init__(self, velocidad_actual, marca, estado):
        self.velocidad_actual = velocidad_actual
        self.marca = marca
        self.estado = estado

    def aumentar_velocidad(self):
        self.velocidad_actual += 10

    def disminuir_velocidad(self):
        self.velocidad_actual -= 6

    def encender(self):
        self.estado = True

    def apagar(self):
        self.estado = False
