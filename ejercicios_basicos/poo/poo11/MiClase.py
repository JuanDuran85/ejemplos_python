# trabajando con variables de clase en python

class MiClase:
    # atributos de clase. La variable es de clase, se asocia con la clase y se comprate con todos los objetos que se creen en la clase
    variable_clase = "variable de clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # metodos estaticos. Se asocia con la clase y no con los objetos. No accede a las varibales de la instancia 
    @staticmethod
    def metodo_estatico():
        print("Accediendo a varibale de clase desde el metodo estatico: {}".format(MiClase.variable_clase))
        print("metodo estatico")
        print("No puede modificar el estado de la clase o instancias, metodo de utileria")

    # metodos de clase. Se asocia con la clase y no con los objetos.
    @classmethod
    def metodo_clase(cls):
        print("Accediendo a varibale de clase desde el metodo de clase: {}".format(cls.variable_clase))
        print("metodo clase")

    # metodos de instancia. Se asocia con los objetos y no con la clase. Accede a las varibales de la instancia
    def metodo_instancia(self):
        print("Accediendo a varibale de instancia desde el metodo de instancia: {}".format(self.variable_instancia))
        print("metodo instancia")
        print("Accediendo a varibale de clase desde el metodo de instancia: {}".format(self.variable_clase))
        print("Accediendo al metodo de clase desde el metodo de instancia: {}".format(self.metodo_clase))
        print("Accediendo al metodo estatico desde el metodo de instancia: {}".format(self.metodo_estatico))

# para acceder a la variable de clase, no es necesario crear una instancia de la clase
print(MiClase.variable_clase)

miClase1 = MiClase("variable de instancia 1")
print(miClase1.variable_instancia)
print(miClase1.variable_clase)

MiClase.variable_clase = "variable de clase modificada"
MiClase.variable_clase2_nueva = "variable de clase nueva"

print(MiClase.variable_clase)
print(MiClase.variable_clase2_nueva)
print(miClase1.variable_clase)
print(miClase1.variable_clase2_nueva)
miClase1.metodo_instancia()

miClase2 = MiClase("variable de instancia 2")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
print(miClase2.variable_clase2_nueva)

# llamando el metodo estatico
MiClase.metodo_estatico()

# llamando el metodo de clase
MiClase.metodo_clase()

# modificando el valor de la variable de clase desde una instancia
miClase2.variable_clase = "variable de clase modificada desde instancia"

print(f"{miClase2.variable_clase = }")
print(f"{MiClase.variable_clase = }")

# para imprimir la variable de clase desde la instancia, se debe utilizar __class__
print(f"{miClase2.__class__.variable_clase = }")


# ----------------------------------------------------------------------------------------
# contador de instancias erroneo con variable de clase

class ContadorObjetoErroneo:
    numero_instancia: int = 0
    
    def __init__(self) -> None:
        # al utilizar el mismo nombre que la variable de clase, se genera el solapamiento de variables al crear las instancias
        self.numero_instancia += 1

print("Contador de Instancias errorneo")
print("Se llama directamente la variable de clase antes de crear una instancia")
print(ContadorObjetoErroneo.numero_instancia)
print("Se crea una instancia y se llama a la varibale de clase")
print(ContadorObjetoErroneo().numero_instancia)
print("Se crea una segunda instancia y se llama a la varibale de clase")
# se puede observar como nunca aumenta el valor del contador en 1
print(ContadorObjetoErroneo().numero_instancia)

# ----------------------------------------------------------------------------------------
# contador de instancias con variable de clase correcto

class ContadorObjetoCorrecto:
    numero_instancia: int = 0
    
    def __init__(self) -> None:
        # existen dos maneras de acceder a la variable de clase
        # 1. ContadorObjetoCorrecto.numero_instancia
        # 2. self.__class__.numero_instancia
        ContadorObjetoCorrecto.numero_instancia += 1
        
print("\nContador de Instancias correcto")
print("Se llama directamente la variable de clase antes de crear una instancia")
print(ContadorObjetoCorrecto.numero_instancia)
print("Se crea una instancia y se llama a la varibale de clase")
print(ContadorObjetoCorrecto().numero_instancia)
print("Se crea una segunda instancia y se llama a la varibale de clase")
print(ContadorObjetoCorrecto().numero_instancia)

# ----------------------------------------------------------------------------------------
# metodos de clase, instancia y static
print("\n\r\t")
class ClasePrincipal:
    """sumary_line: Clase Principal
    Keyword arguments: None
    Return: None
    Description: Static, class and instance methods
    """
    
    ''' este metodo recibe el paremtro de self, ya que es un metodo de instancias y recibe la instancia que se va a ejecutar en el momento que se llama el metodo '''
    def metodo_instancia(self) -> tuple:
        # retornamos una tupla de valores
        return "Metodo de Instancia Ejecutado... ", self, self.__class__.__name__

    ''' Para los metodos de clase se usa el decorador classmethod, el metodo recibe como argumento la palabra reservada cls para hacer referencia a la clase. Por lo tanto, el metodo debe recibir la clase como parametro para que pueda ejecutarse, por lo que puede acceder a los atributos y metodos de instancia de la clase '''
    @classmethod
    def metodo_de_clase(cls) -> tuple:
        return "Metodo de clase Ejecutado... ", cls, cls.__name__
    
    
    '''  Metodo estatico, se usa el decorador de staticmethod, no reciben ningun parametro y no tienen acceso ni a la informacion de la isntancia ni de la clase'''
    @staticmethod
    def metodo_estatico() -> str:
        return "Metodo Estatico Ejecutado... "
    
    

# Caso 1: Ejecutamos el metodo de instancia de manera implicita como normalmente se hace
objeto_uno: ClasePrincipal = ClasePrincipal()
print(objeto_uno.metodo_instancia())

# Caso 2: Ejecutamos el metodo de instancia de manera explicita
# Se debe pasar la referencia, es decir, la instancia creada para que se puede ejecutar de manera correcta el metodo
print(ClasePrincipal.metodo_instancia(objeto_uno))

# Caso 3: Ejecutamos el metodo de clase, el cual, pasa la clase de manera implicita
print(ClasePrincipal.metodo_de_clase())

# Caso 4: Desde las instancias podemos acceder a los metodos de clase
print(objeto_uno.metodo_de_clase())

# Caso 5: Para llamar al metodo estatico, se puede hacer desde la misma clase
print(ClasePrincipal.metodo_estatico())

# Caso 6: El metodo estatico tambien se puede acceder desde la instancia
print(objeto_uno.metodo_estatico())