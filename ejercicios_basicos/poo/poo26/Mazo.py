"""_summary_

    Juego de Cartas con POO

"""

from Carta import Carta

class Mazo:
    def __init__(self) -> None:
        self.crear_mazo()
        
    def crear_mazo(self) -> None:
        mazos: list = ["Treboles","Diamantes","Espadas","Corazones"] 
        for mazo in mazos:
            for i in range(1,14):
                carta: Carta = Carta(i, mazo)
                carta.imprimir()

if __name__ == '__main__':
    mazo1: Mazo = Mazo()