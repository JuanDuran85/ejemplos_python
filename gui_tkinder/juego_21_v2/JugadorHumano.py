"""_summary_

    Juego de Cartas con POO

"""

from Mazo import Mazo
from Interfaz import Interfaz
from Jugador import Jugador

class JugadorHumano(Jugador):

    def solicitar_carta(self,mazo) -> int:
         self.cartas.append(mazo.obtener_siguiente_carta())
         return self.sumar_cartas()
    
    def jugar(self, mazo: Mazo) -> int:
        interfaz: Interfaz = Interfaz()
        solicitar: bool = True
        titulo: str = "Digite:\n1- Pedir Carta\n2- Quedarse\nValor: "
        
        while(solicitar and self.sumar_cartas() <= 21):
            self.imprimir()
            valor: int = interfaz.solicitar_numero_entero(titulo)
            if (valor == 1):
                self.cartas.append(mazo.obtener_siguiente_carta())
                self.cartas[-1].imprimir()
            elif (valor == 2):
                solicitar = False
                print(self.sumar_cartas())
                print("Gracias por Jugar")
            else:
                print("Ingrese un valor valido")
        print(self.sumar_cartas())
        return self.sumar_cartas()
                
if __name__ == '__main__':
    mazo: Mazo = Mazo()
    jugador_uno: JugadorHumano = JugadorHumano("Juan", [])
    jugador_uno.jugar(mazo)