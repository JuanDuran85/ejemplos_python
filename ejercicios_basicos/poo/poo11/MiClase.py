# trabajando con variables de clase en python

class MiClase:
    # atributos de clase. La variable es de clase, se asocia con la clase y se comprate con todos los objetos que se creen en la clase
    variable_clase = "variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # metodos estaticos. Se asocia con la clase y no con los objetos. No accede a las varibales de la instancia 
    @staticmethod
    def metodo_estatico():
        print("Accediendo a varibale de clase desde el metodo estatico: {}".format(MiClase.variable_clase))
        print("metodo estatico")

    # metodos de clase. Se asocia con la clase y no con los objetos.
    @classmethod
    def metodo_clase(cls):
        print("Accediendo a varibale de clase desde el metodo de clase: {}".format(cls.variable_clase))
        print("metodo clase")

    # metodos de instancia. Se asocia con los objetos y no con la clase. Accede a las varibales de la instancia
    def metodo_instancia(self):
        print("Accediendo a varibale de instancia desde el metodo de instancia: {}".format(self.variable_instancia))
        print("metodo instancia")
        print("Accediendo a varibale de clase desde el metodo de instancia: {}".format(self.variable_clase))
        print("Accediendo al metodo de clase desde el metodo de instancia: {}".format(self.metodo_clase))
        print("Accediendo al metodo estatico desde el metodo de instancia: {}".format(self.metodo_estatico))

# para acceder a la variable de clase, no es necesario crear una instancia de la clase
print(MiClase.variable_clase)

miClase1 = MiClase("variable de instancia 1")
print(miClase1.variable_instancia)
print(miClase1.variable_clase)

MiClase.variable_clase = "variable de clase modificada"
MiClase.variable_clase2 = "variable de clase nueva"

print(MiClase.variable_clase)
print(MiClase.variable_clase2)
print(miClase1.variable_clase)
print(miClase1.variable_clase2)
miClase1.metodo_instancia()

miClase2 = MiClase("variable de instancia 2")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
print(miClase2.variable_clase2)

# llamando el metodo estatico
MiClase.metodo_estatico()

# llamando el metodo de clase
MiClase.metodo_clase()