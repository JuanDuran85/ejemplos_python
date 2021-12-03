# simulacion de sobreacarga de constructores en python
# otras formas de crear objetos en python

class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)  # llama al metodo init de manera indirecta
    
    @classmethod
    def crear_persona_con_valores(cls, nombre, edad):
        return cls(nombre, edad)  # llama al metodo init de manera indirecta pasando los valores
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

persona1 = Persona("Juan", 23)
print(persona1)
persona_vacio = Persona.crear_persona_vacia()
print(persona_vacio)
persona_con_valores = Persona.crear_persona_con_valores("Pedro", 25)
print(persona_con_valores)