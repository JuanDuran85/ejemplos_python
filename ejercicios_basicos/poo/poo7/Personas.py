# trabajando con encapsulamiento eb python

class Persona:
    def __init__(self, nombre, apellido, edad):
        # se puede utilizar uno o dos _ para indicar que el atributo sera encapsulado
        # si se utilizan los dos __ no se puede acceder a el
        self.__nombre = nombre
        self.__apellido = apellido
        self.edad = edad
    
    # para encapsular una propiedad se utiliza el decorador @property en un metodo del tipo get
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    
    # como no existe un metodo setter para el atributo apellido, seria entonces un atributo de solo lectura

    def mostrar_detalles(self):
        print(f"El nombre es: {self.nombre} y la edad: {self.edad}")

persona1 = Persona("Juan", 23)
persona1.mostrar_detalles()
print(persona1.nombre)
persona1.nombre = "Pedro"
print(persona1.nombre)
persona1.mostrar_detalles()

