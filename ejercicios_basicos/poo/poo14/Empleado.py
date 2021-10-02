# trabajando con pilimorfismo

class Empleado:
    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def sueldo(self):
        return self.__sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self.__sueldo = sueldo

    def mostrar_detalle(self):
        print("En clase padre Empleado")

    def __str__(self):
        return "El empleado: {}, tiene un sueldo de: {} USD.".format(self.nombre, self.sueldo)