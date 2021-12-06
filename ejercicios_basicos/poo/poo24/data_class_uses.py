
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Persona:
    nombre: str
    edad: int
    contador: ClassVar[int] = 0
    
persona1 = Persona('Juan', 20)
print(persona1)
# variales de clase
print(persona1.contador)
# varibale de instancia
print(persona1.__dict__)