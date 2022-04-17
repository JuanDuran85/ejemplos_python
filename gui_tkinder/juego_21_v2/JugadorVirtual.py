"""_summary_

    Juego de Cartas con POO

"""

from Mazo import Mazo
from Jugador import Jugador

class JugadorVirtual(Jugador):
    
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