"""_summary_

    Patron Creacional Singleton: consiste en utilizar una sola instancia de clase, definiendo asi un unico punto global de acceso a ella. Dicha instancia es la encargada de la inicializacion, creacion y acceso a las propiedades de clase.

"""

class SingletonPattern():
    
    @staticmethod
    def singleton(cls):
        instance = dict()
        def wrapper(*args, **kwargs):
            if cls not in instance:
                instance[cls] = cls(*args, **kwargs)
            return instance[cls]
        return wrapper

@SingletonPattern.singleton  
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
persona1 = Person("Juan", 30)
persona2 = Person("Maria", 25)

print(persona1)
print(persona2)

# para verificar si son la misma instancia de clase
print(persona1 is persona2)