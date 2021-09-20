# trabajando con encapsulamiento eb python

class Persona:
    def __init__(self, nombre, apellido, edad):
        # se puede utilizar uno o dos _ para indicar que el atributo sera encapsulado
        # si se utilizan los dos __ no se puede acceder a el
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
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
    
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.__edad = edad

    # como no existe un metodo setter para el atributo apellido, seria entonces un atributo de solo lectura

    def mostrar_detalles(self):
        print(f"El nombre es: {self.nombre}, el apellido es: {self.apellido} y la edad: {self.edad}")

persona1 = Persona("Omer", "Dach", 23)
persona1.mostrar_detalles()
print(persona1.nombre)
persona1.nombre = "Pedro"
print(persona1.nombre)
persona1.edad = 50
persona1.mostrar_detalles()