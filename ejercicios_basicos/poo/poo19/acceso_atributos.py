# atributos publicos, privados y protegidos

class MiClase:
    def __init__(self):
        self.atributo_publico = "valor publico"
        self._atributo_protegido = "valor protegido"
        self.__atributo_privado = "valor privado"
        
objeto1 = MiClase()

# acceso a los atributos publicos
print(objeto1.atributo_publico)
# modificando atributos publicos
objeto1.atributo_publico = "otro valor"
print(objeto1.atributo_publico)

# acceso a los atributos protegidos
print(objeto1._atributo_protegido)
# modificando atributo protegido
objeto1._atributo_protegido = "otro nuevo valor"
print(objeto1._atributo_protegido)

# acceso a atributo privado
try:
    print(objeto1.__atributo_privado)
except AttributeError:
    print("No se puede acceder al atributo privado")
    
# python convierte el atributo privado a: objeto._clase__atributo_privado
print(objeto1._MiClase__atributo_privado)
objeto1._MiClase__atributo_privado = "Nuevo valor privado"
print(objeto1._MiClase__atributo_privado)