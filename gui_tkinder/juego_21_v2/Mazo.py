"""_summary_

    Juego de Cartas con POO

"""

from Carta import Carta
import random

class Mazo:
    def __init__(self) -> None:
        self.cartas: list = []
        self.ultima_repartida: int = 0
        self.crear_mazo()
        
    def crear_mazo(self) -> None:
        mazos: list = ["Treboles","Diamantes","Espadas","Corazones"]
        self.ultima_repartida: int = 0
        for mazo in mazos:
            for i in range(1,14):
                carta: Carta = Carta(i, mazo)
                self.cartas.append(carta)
                
    def revolver(self) -> None:
        for celda in range(len(self.cartas)):
            aleatorio: int = random.randint(0, len(self.cartas)-1)
            (self.cartas[celda],self.cartas[aleatorio]) = (self.cartas[aleatorio],self.cartas[celda])
    
    def imprimir(self) -> None:
        for instancia_carta in self.cartas:
            instancia_carta.imprimir()
            
    def obtener_siguiente_carta(self) -> Carta:
        carta: Carta = self.cartas[self.ultima_repartida]
        self.ultima_repartida += 1
        return carta

if __name__ == '__main__':
    mazo1: Mazo = Mazo()
    mazo1.imprimir()
    print("----------------------------------------------")
    
    mazo1.obtener_siguiente_carta().imprimir()
    mazo1.obtener_siguiente_carta().imprimir()
    mazo1.obtener_siguiente_carta().imprimir()
    mazo1.obtener_siguiente_carta().imprimir()