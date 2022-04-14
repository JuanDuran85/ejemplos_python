"""_summary_

    Juego de Cartas con POO

"""

from Carta import Carta
from Mazo import Mazo
from Interfaz import Interfaz

class JugadorVirtual:
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
    
    def imprimir_juego(self) -> None:
        cartas: list = ['_']
        for i in range(1,len(self.cartas)):
            cartas.append(self.cartas[i].numero)
        print(cartas)
        
    def jugar(self, mazo: Mazo) -> int:
        while(self.sumar_cartas() < 16):
            self.cartas.append(mazo.obtener_siguiente_carta())
        self.imprimir_juego()
        return self.sumar_cartas()
                
        
if __name__ == '__main__':
    mazo: Mazo = Mazo()
    jugador_uno: JugadorVirtual = JugadorVirtual("Juan", [])
    jugador_uno.jugar(mazo)