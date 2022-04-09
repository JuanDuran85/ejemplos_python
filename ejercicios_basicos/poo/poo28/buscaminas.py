"""_summary_

    Juego Buscaminas

"""

import random

class Buscaminas:
    def __init__(self,filas: int, columna: int) -> None:
        self.tablero: list = [None]*filas
        self.tablero_usuario: list = [None]*filas
        
        for i in range(filas):
            self.tablero[i] = [0] * columna
            self.tablero_usuario[i] = [0] * columna
    
    def colocar_mina(self, minas: int) -> None:
        while (minas > 0):
            fila: int = random.randint(0,len(self.tablero)-1)
            columna: int = random.randint(0,len(self.tablero[fila])-1)
            if( self.tablero[fila][columna] == 0 ):
                self.tablero[fila][columna] = -1
                minas -= 1
    
    
    def colocar_numeros(self) -> None:
        filas: list = [0,0,-1,1,1,1,-1,-1,]
        columnas: list = [1,-1,0,0,1,-1,1,-1]
        
        for f in range(len(self.tablero)):
            for c in range(len(self.tablero[f])):
                if(self.tablero[f][c] == -1):
                    contador: int = 0
                    while (contador < 8):
                        nueva_fila = f + filas[contador]
                        nueva_columna = c + columnas[contador]
                        if(nueva_fila >= 0 and nueva_fila < len(self.tablero) and nueva_columna >= 0 and nueva_columna < len(self.tablero[nueva_fila]) and self.tablero[nueva_fila][nueva_columna] != -1):
                            self.tablero[nueva_fila][nueva_columna] += 1
                        contador += 1
            
    def __str__(self) -> str:
        contenido: str = ""
        
        for f in range(len(self.tablero)):
            for c in range(len(self.tablero[f])):
                if (self.tablero[f][c] == -1 ):
                    contenido += ("M\t")
                else:
                    contenido += str(self.tablero[f][c]) + "\t"
            contenido += "\n"    
        return contenido
    
if __name__ == '__main__':
    buscaminas: Buscaminas = Buscaminas(5,6)
    print(buscaminas)
    buscaminas.colocar_mina(10)
    print(buscaminas)
    buscaminas.colocar_numeros()
    print(buscaminas)
    