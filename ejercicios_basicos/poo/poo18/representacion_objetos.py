# representacion de un objeto con str, repr, format

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # enfocado mas al programador
    def __repr__(self):
        return f"{self.__class__.__name__}(nombre:{self.nombre}, edad:{self.edad})"
    
    # el str es mas para el usuario final u otros sistemas. 
    # la implementacion por defecto es el __repr__
    def __str__(self):
        return f"{self.__class__.__name__}. {self.nombre} tiene {self.edad} años"
    
    # metodo format, por defecto manada a llamar el metodo str al menos que se use un string para llamarlo como f string
    def __format__(self, format_spec):
        return f"Nombre de la clase: {self.__class__.__name__}. Atributos: ({self.nombre}, {self.edad})"

    
persona1 = Persona("Juan", 23)
print(f"El objeto persona1 con metodo repr es: {persona1!r}") # !r para asegurarse que llama el metodo repr
print(persona1) # llama el metodo str
print(f"El objeto persona1 con format es: {persona1:f}") # llama el metodo format