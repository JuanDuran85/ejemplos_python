from Empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento

    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento
    
    def mostrar_detalle(self):
        print("En clase hija Gerente")

    def __str__(self):
        return super().__str__() + f'\nPertece al Departamento: {self.departamento}'