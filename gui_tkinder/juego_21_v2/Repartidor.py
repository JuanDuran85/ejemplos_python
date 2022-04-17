"""_summary_

    Juego de Cartas con POO

"""

from Mazo import Mazo
from Jugador import Jugador
from JugadorVirtual import JugadorVirtual

class Repartidor:
    
    def __init__(self, lista_jugadores: list) -> None:
        self.jugadores: list = lista_jugadores
        self.resultados: list = []
        self.mazo: Mazo = Mazo()
        
    def repartir_cartas(self) -> None:
        for jugador in self.jugadores:
            cartas: list = [self.mazo.obtener_siguiente_carta(), self.mazo.obtener_siguiente_carta()]
            jugador.asignar_cartas(cartas)
            
    def jugar(self) -> None:
        ganador: int = 0
        valor: int = 0
        self.mazo.revolver()
        self.repartir_cartas()
        print(f"Existen {len(self.jugadores)} jugadores en la partida")
        for i in range(len(self.jugadores)):
            suma: int = self.jugadores[i].jugar(self.mazo)
            resultado: int = 21 -suma
            if((resultado > valor and resultado < 0) or (resultado == valor and len(self.jugadores[i].cartas) < len(self.jugadores[ganador].cartas))):
                valor = resultado
                ganador = i
            print(f"la suma de {i} es {suma}")
            self.resultados.append(resultado)
        print(f"Los resultados son {self.resultados}, {self.jugadores[ganador].nombre} gana, con {valor}")   
    
    
    def iniciar_juego(self) -> dict:
        self.mazo.revolver()
        self.repartir_cartas()
        return {
            'j1': self.jugadores[0].cartas,
            'jv': self.jugadores[1].cartas,
        }
        
    def determinar_ganador(self) -> bool:
        ganador: int = 0
        valor: int = 21
        for i in range(len(self.jugadores)):
            suma: int = self.jugadores[i].sumar_cartas()
            resultado: int = 21 - suma
            if(resultado < valor and resultado >= 0):
                valor = resultado
                ganador = i
                
        return ganador == 0

if __name__ == '__main__':
    j1: Jugador = Jugador("Juan")
    j2: JugadorVirtual = JugadorVirtual("Computadora 1")
    
    repartidor: Repartidor = Repartidor([j1,j2])
    repartidor.jugar()
    