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
            self.tablero_usuario[i] = ["_"] * columna
    
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
            
        contenido += " - - Tablero Usuario\n"
        
        for f in range(len(self.tablero_usuario)):
            for c in range(len(self.tablero_usuario[f])):
                contenido += str(self.tablero_usuario[f][c]) + "\t"
            contenido += "\n"
         
        return contenido
    
    def colocar_pieza(self, fila_in: int, columna_in: int, pierde: bool = True) -> None:
        filas: list = [0,0,-1,1,1,1,-1,-1,]
        columnas: list = [1,-1,0,0,1,-1,1,-1]
        
        if(fila_in >= 0 and fila_in < len(self.tablero) and columna_in >= 0 and columna_in < len(self.tablero[fila_in])):
            if (self.tablero_usuario[fila_in][columna_in] == '_' and self.tablero[fila_in][columna_in] == 0):
                self.tablero_usuario[fila_in][columna_in] = str(self.tablero[fila_in][columna_in])
                contador: int = 0
                while(contador < 8):
                    nueva_fila = fila_in + filas[contador]
                    nueva_columna = columna_in + columnas[contador]
                    pierde = self.colocar_pieza(nueva_fila, nueva_columna, False)
                    contador += 1
            elif (self.tablero[fila_in][columna_in] > 0):
                self.tablero_usuario[fila_in][columna_in] = str(self.tablero[fila_in][columna_in])
                pierde = False
            else:
                self.tablero_usuario[fila_in][columna_in] = str(self.tablero[fila_in][columna_in])
        return pierde
    
if __name__ == '__main__':
    buscaminas: Buscaminas = Buscaminas(5,6)
    print(buscaminas)
    buscaminas.colocar_mina(3)
    print(buscaminas)
    buscaminas.colocar_numeros()
    print(buscaminas)
    buscaminas.colocar_pieza(0,0)
    print(buscaminas)
    