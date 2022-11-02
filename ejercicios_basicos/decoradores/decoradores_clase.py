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
        
    #crear el metodo repr
    def metodo_repr(self):
        #obtenemos el nombre de la clase dinamicamente
        nombre_clase = self.__class__.__name__
        print("nombre_clase: ", nombre_clase)
        # obetenemos los nombres de las propiedades y sus valores dinamicamente
        # expresion generadora para crear la siguiente cadena con la forma del nombre del atributo
        generador_argumentos = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        print("generador_argumentos: ", generador_argumentos)
        # crear lista de argumentos
        lista_argumentos = list(generador_argumentos)
        print("lista_argumentos: ", lista_argumentos)
        # creamosla cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_argumentos)
        print("argumentos: ", argumentos)
        # creamos la forma del metodo repr sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        return resultado_metodo_repr
    
    #agregamos dinamicamente el metodo repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)
        
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
print(persona1)
# tiene los metodos de la propiedad
print(dir(persona1))
# tiene el metodo repr sobre escrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)

#-----------------------------------------------------------------------------------
# class decorator with arguments. Using a class like decorator on a function
#-----------------------------------------------------------------------------------
class decorator_with_arguments:
    def __init__(self,arg1,arg2):
        print('In __init__ class')
        self.arg1 = arg1
        self.arg2 = arg2
        print(f"Decorator args: {arg1} |-| {arg2}")
        
    def __call__(self,func_in):
        print("In __call__ class")
        def wrapper(*args, **kwargs):
            print("In wrapper method")
            new_args = args[0] + 5
            return func_in(new_args)
        return wrapper

@decorator_with_arguments(3,'Python')
def doubler_fn(number_in):
    return number_in * 2

print(doubler_fn(5))

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------