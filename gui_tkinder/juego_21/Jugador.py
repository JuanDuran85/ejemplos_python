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
    jugador_uno: Jugador = Jugador("Juan", [])
    jugador_uno.jugar(mazo)