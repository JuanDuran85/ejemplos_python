class Persona:
    contador_personas = 0

    @classmethod
    def generar_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "--> Id: {}, Nombre: {}, Edad: {}".format(self.id_persona,self.nombre, self.edad)

persona1 = Persona("Juan", 20)
persona2 = Persona("Pedro", 30)
persona3 = Persona("Ana", 40)
print(persona1)
print(persona2)
print(persona3)
print("Total personas: {}".format(Persona.contador_personas))