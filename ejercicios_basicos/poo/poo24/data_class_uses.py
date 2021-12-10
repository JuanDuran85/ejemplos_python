from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True,frozen=True)
class Domicilio:
    calle: str
    numero: int = 0


# dataclasses tiene por defecto eq en true, el frozen por defecto es en false, ya que se pueden modificar
@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    edad: int = 0
    contador: ClassVar[int] = 0
    
    def __post_init__(self):
        if not self.nombre:
            raise ValueError("El nombre no puede ser vacio")
    
    
domicilio1 = Domicilio("Calle Falsa 123")    
persona1 = Persona('Juan', 'Duran', domicilio1 ,20)
print(persona1)
# variales de clase
print(persona1.contador)
# varibale de instancia no incluye la variable de clase
print(persona1.__dict__)
# creando una variable con valores vacios
persona_vacia = Persona('Karla','','')
print(persona_vacia)
# revisar igualdad de objetos (__eq__)
persona2 = Persona('Juan', 'Duran', Domicilio('Calle Falsa 123') ,20)
print(persona1 == persona2)
# para crear una coleccion de objetos se dede modificar el frozen en true, ya que permiten tipo inmutables
coleccion = {persona1, persona2}
print(coleccion)