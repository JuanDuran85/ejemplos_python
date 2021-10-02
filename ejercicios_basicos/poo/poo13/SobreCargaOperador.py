# trabajando con sobre carga de operadores para una clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "{} tiene {} años".format(self.nombre, self.edad)

    def __add__(self, other):
        return "Al unir los nombres se tiene: {} {}".format(self.nombre, other.nombre)

    def __sub__(self, other):
        return "Al restar las edades se tiene: {}".format(self.edad - other.edad)

persona1 = Persona("Juan", 20)
persona2 = Persona("Pedro", 30)

print(persona1 + persona2)
print(persona1 - persona2)