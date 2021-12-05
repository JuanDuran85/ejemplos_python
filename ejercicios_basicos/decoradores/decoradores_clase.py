import inspect

''' 
Decoradores de clases por Meta programacion 

Permiten trasnformar una clase de manera programatica
Es simal a los decoradores de funciones

'''
# creando decorador
def decorador_repr(cls):
    print('Decorador de clase')
    print(cls.__name__)
    
    # revisamos los atributos de la clase
    atributos = vars(cls)
    
    # iteramos los atributos
    for (nombre,atributo) in atributos.items():
        print(nombre,atributo)
        
    # revisamos si se ha sobreescrito el metodo init
    if '__init__' not in atributos:
        print('No se ha sobreescrito el metodo init')
        raise TypeError("No se ha sobreescrito el metodo init")
        
    # recuperar la firma del metodo init para saber los parametros
    firma_init = inspect.signature(cls.__init__)
    print('Firma del metodo init: ', firma_init)
    
    # recuperar los parametros del init menos el self
    parametros_init = list(firma_init.parameters)[1:]
    print('Parametros del init: ', parametros_init)
        
    # revisar si por cada parametro existe un metodo property asociado
    for parametro in parametros_init:
        es_metodo_propiedad = isinstance(atributos.get(parametro), property)
        if not es_metodo_propiedad or parametro not in atributos:
            print('No existe el atributo: ', parametro)
            raise TypeError("No existe el atributo: ", parametro)
        
    # retornamos la clase
    return cls

# agregando decorador
@decorador_repr
# creando clase
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre


# creando instancia de la clase
persona1 = Persona("Juan", 25)
