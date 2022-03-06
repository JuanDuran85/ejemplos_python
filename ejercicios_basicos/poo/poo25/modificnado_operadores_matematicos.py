"""_summary_
 
    Modificando Operadores Matematicos desde una clase

"""

class Operadores:
    
    def __init__(self, lista_numeros: list) -> None:
        self.lista_numeros = lista_numeros
        
    def visualizar(self) -> None:
        print(self.lista_numeros)
        
    def __add__(self, numero_entero: int) -> list:
        nueva_lista: list = []
        for x in range(len(self.lista_numeros)):
            nueva_lista.append(self.lista_numeros[x] + numero_entero)
        return nueva_lista
    
    def __sub__(self, numero_entero: int) -> list:
        nueva_lista: list = []
        for x in range(len(self.lista_numeros)):
            nueva_lista.append(self.lista_numeros[x] - numero_entero)
        return nueva_lista
    
    def __mul__(self, numero_entero: int) -> list:
        nueva_lista: list = []
        for x in range(len(self.lista_numeros)):
            nueva_lista.append(self.lista_numeros[x] * numero_entero)
        return nueva_lista
    
    def __floordiv__(self, numero_entero: int) -> list:
        nueva_lista: list = []
        for x in range(len(self.lista_numeros)):
            nueva_lista.append(self.lista_numeros[x] // numero_entero)
        return nueva_lista
    
if __name__ == '__main__':
    datos = Operadores([14, 52, 36])
    datos.visualizar()
    print(datos + 10)
    print(datos - 10)
    print(datos * 10)
    print(datos // 10)