# ejemplo de herencia simple

class ListaSimple:
    def __init__(self, elementos):
        self.__elementos = list(elementos)
        
    def agregar(self, elemento):
        self.__elementos.append(elemento)
    
    # permite recuperar un elemento (metodo build-in definido en el tipo list)    
    def __getitem__(self, indice):
        return self.__elementos[indice]
    
    def ordenar(self):
        self.__elementos.sort()
        
    # metodo build-in definido en el tipo list
    def __len__(self):
        return len(self.__elementos)
    
    # representar el objeto como un string
    def __repr__(self):
        return f"{self.__class__.__name__}--->({self.__elementos!r})"
    
# clase hija de la clase ListaSimple
class ListaOrdenada(ListaSimple):
    def __init__(self, elementos = []):
        super().__init__(elementos)
        # se ordena la lista una vez inicializada
        self.ordenar()
        
    def agregar(self, elemento):
        super().agregar(elemento)
        # se ordena la lista una vez inicializad
        self.ordenar()


class ListaEnteros(ListaSimple):
    def __init__(self, elementos = []):
        for element in elementos:
            self.__validar_numero(element)
        # una vez validados los elementos, se agregan a la lista    
        super().__init__(elementos)
        # se ordena la lista una vez inicializada
        
    def agregar(self, elemento):
        super().agregar(elemento)

    def __validar_numero(self, elemento):
        # validamos si el elemento es del tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f"El elemento debe ser un numero entero {elemento}")
        
    # sobreEscribimos el metodo agregar de la clase padre
    def agregar(self, elemento):
        self.__validar_numero(elemento)
        # una vez validado lo agregamos a la lista
        super().agregar(elemento)

# Lista de enterors ordenada con herencia multiple.
# el orden de la herencia es importante, la primera tomara el control
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

#creando objeto de la clase ListaSimple - Lista Simple
lista_simple = ListaSimple([4,6,7,3,2])
print(lista_simple)
#creando una lista ordenada
lista_ordenada = ListaOrdenada([4,6,7,3,2])
print(lista_ordenada)
lista_ordenada.agregar(1)
print(lista_ordenada)
lista_ordenada.agregar(14)
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))
print(lista_ordenada[0])
#creando una lista de enteros
lista_enteros = ListaEnteros([4,6,7,3,2])
print(lista_enteros)
#creando lista de enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,-6,7,3,-2,45,65,21,1,-1,-7])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(11)
print(lista_enteros_ordenada)

# saber las clases padres y su orden de herencia. 
print(ListaEnterosOrdenada.__bases__)

''' MRO - Method Resolution Order '''
# MRO (method resolution order)
print(ListaEnterosOrdenada.__mro__)

# usando el metodo isinstance para saber si un objeto es de una clase
print('Es una lista de enteros ordenadas \'lista simple\'?: ', isinstance(lista_simple, ListaEnterosOrdenada))