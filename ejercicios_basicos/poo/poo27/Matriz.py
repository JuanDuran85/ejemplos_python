"""_summary_

    Generando una matriz identidad con clases

"""

class Matriz:
    
    def generar_identidad(self,n:int) -> list or None:
        if n <= -1:
            return None
        matriz_final: list = []
        lista_interna: list = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    lista_interna.append(1)
                else:
                    lista_interna.append(0)
            matriz_final.append(lista_interna)
            lista_interna = []
        return matriz_final
            
matriz_uno: Matriz = Matriz()
print(matriz_uno.generar_identidad(5))