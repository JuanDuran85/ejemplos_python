"""[summary]

Tips and tricks for class -POO in Python.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""
"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using inheritance'''
print("\n Using inheritance \n")

# If you need know one class is a subclass of another, you can use the issubclass method.
class Vehicle:
    def __init__(self, year, model):
        self.year = year
        self.model = model

class Car(Vehicle):
    def __init__(self, year, model, color):
        super().__init__(year, model)
        self.color = color
        
print(f"{issubclass(Car, Vehicle) = }")
print(f"{issubclass(Vehicle, Car) = }")

print("\n Using __len__ method \n")

# To get the length of the class, you can use the __len__ method.

class Cart:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)

c = Cart("Hello")
print(f"{len(c) = }")

print("\n Using hasattr and getattr methods \n")

# If you want to know if a class has any attributes or get any attributes, you can use the hasattr and getattr methods.

class Job:
    def __init__(self, name, title):
        self.name = name
        self.title = title
        
job = Job("Juan","Developer")
print(f"{hasattr(job, 'name') = }")
print(f"{hasattr(job, 'title') = }")
print(f"{getattr(job, 'name') = }")
print(f"{getattr(job, 'title') = }")
print(f"{hasattr(job, 'age') = }")


# If you need set a new attribute, you can use the setattr method.

class Animal: ...

cat: Animal = Animal()
print(f"{cat = }")
setattr(cat, 'name', 'Garfield')
print(f"{cat.name = }")

# you can delete a object class with __del__ method.

class Video():
    def __init__(self, title: str, duration: int):
        self.title = title
        self.duration = duration
        print(f"Se creo el video {self.title}")
        
    def __str__(self):
        return f"{self.title} - {self.duration}"
        
    def __del__(self):
        print(f"Se elimino el video {self.title}")
        
    def __len__(self):
        return self.duration
        
video_one: Video = Video("Video 1", 130)
print(video_one)
print(f"La duracion del video es: {len(video_one)}")
del(video_one)

# class in one line
School = type('School', (object,), {'fun':{}})
print(f"{School = }")

# ---------------------------------------------------------------------------------------------
# you can use class and dict to load classes
class ProductionConfig:
    ELASTICSEARCH_URL: str = 'https://elasticsearch.example.com'

class DevelopmentConfig:
    ELASTICSEARCH_URL: str = 'https://development-elasticsearch.example.com'
    
class TestConfig:
    ELASTICSEARCH_URL: str = 'http://localhost:9200'

CONFIGS: dict = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "test": TestConfig
}

def load_config(enviroment):
    return CONFIGS.get(enviroment, DevelopmentConfig)

print(f"{load_config('production') = }")
print(f"{load_config('test') = }")
print(f"{load_config('unknow') = }")
print(f"{load_config('development') = }")

# ---------------------------------------------------------------------------
# con doble guion bajo, no solo es una convencion, ya que afecta la forma en que se acceden a los atributos y metodos

class Padre:
    def __init__(self) -> None:
        self.varible_publica: int = 1
        self._variable_publica: int = 2
        self.__variable_privada: int = 3
        self.__variable_dunder__ = 2 # a estas variables no se le aplica el concepto de name mangling
        
    def get_variable_privada(self) -> int:
        return self.__variable_privada
    
    def get_metodo_privado(self) -> int:
        return self.__metodo_privado()
    
    def __metodo_privado(self) -> int:
        return self.__variable_privada
    
class Hijo(Padre):
    def __init__(self) -> None:
        super().__init__()
        self.varible_publica: str = 'Variable sobreescrita 1'
        self._variable_publica: str = 'Variable sobreescrita 2'
        self.__variable_privada: str = 'Variable sobreescrita 3'
        
padre: Padre = Padre()
print(dir(padre))
# esto imprime para la variable privada: '_Padre__variable_privada', lo cual se denomina 'Name Mangling', para evitar conflictos que se hereden de las clases
print(f"Variable privada: {padre._Padre__variable_privada}")
print(f"metodo privado: {padre.get_metodo_privado()}")
hijo: Hijo = Hijo()
print(hijo.get_variable_privada())
print(hijo.varible_publica)
print(hijo._Hijo__variable_privada)

# ----------------------------------------------------------------------------------------------
# sobreescritura de metodo call en una clase
# Si se quiere que una clase defina objetos que se puedan llamar como una funcion, se debe sobreescribir el metodo call

class Mostrar:
    def __init__(self,titulo: str) -> None:
        self.titulo: str = titulo

    def __call__(self, mensaje: str) -> str:
        return f"{self.titulo} {mensaje}"
    
mostrar: Mostrar = Mostrar("Sr.")
print(mostrar("Juan"))


# ----------------------------------------------------------------------------------------------
# Utilizando clases para hacer validaciones personalizadas de errores.

# Ejemplo para validar el largo de una cadeda de texto
class ValidandoErrorClase(ValueError):
    pass

def largo_cadena_validacion(texto: str) -> bool:
    if len(texto) < 3:
        raise ValidandoErrorClase(f"El largo de la cadena -'{texto}'- debe ser mayor a 3")
    else:
        return True
    
cadena_texto: str = "Mensaje nuevo"
print(largo_cadena_validacion(cadena_texto))

# ----------------------------------------------------------------------------------------------
# Utilizando clases para hacer validaciones personalizadas de errores, pero creando una clase base y de alli extender a las otras clases.
    
class ExceptionBaseClase(TypeError):
    pass

class LengthErrorClase(ExceptionBaseClase):
    pass

def length_string(text_in: str) -> bool:
    if len(text_in) < 3:
        raise LengthErrorClase(f"El largo de la cadena -'{text_in}'- debe ser mayor a 3")
    else:
        print("La cadena es valida")
        return True
    
try:
    length_string("Me")    
except ExceptionBaseClase as e:
    print(f"{type(e).__name__}, linea: {e.__traceback__.tb_lineno} en {__file__}, siendo el error: {e}")
    
