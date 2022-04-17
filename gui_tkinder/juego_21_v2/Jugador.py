"""_summary_

    Juego de Cartas con POO

"""

from Carta import Carta
from Mazo import Mazo
from Interfaz import Interfaz

class Jugador:
    def __init__(self, nombre: str, cartas: list = None) -> None:
        self.nombre = nombre
        self.cartas = cartas
        
    def asignar_cartas(self, cartas) -> None:
        self.cartas = cartas
        
    def imprimir(self) -> None:
        print(f"{self.nombre} estas son tus cartas")
        for carta in self.cartas:
            carta.imprimir()
        print(f"Suma: {self.sumar_cartas()}")
            
    def sumar_cartas(self) -> int:
        suma: int = 0
        aces: int = 0
        for carta in self.cartas:
            valor: int = carta.obtener_numero()
            if valor == 1:
                aces += 1
            suma += valor
        if (aces > 0 and suma + 10 <= 21):
            suma += 10
        return suma
    
if __name__ == '__main__':
    mazo: Mazo = Mazo()
    jugador_uno: Jugador = Jugador("Juan", [])