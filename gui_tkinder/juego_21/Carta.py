"""_summary_

    Juego de Cartas con POO

"""

class Carta:
    def __init__(self, numero: int, palo: str)-> None:
        self.palo = palo
        self.numero = numero
        
    def imprimir(self)-> None:
        letra_numero: str = self.convertir_numero_a_letras()
        print(f"{letra_numero} de {self.palo}")
        
    def convertir_numero_a_letras(self) -> str:
        valor: str = ""
        if (self.numero == 11):
            valor = "J"
        elif (self.numero == 12):
            valor = "Q"
        elif (self.numero == 13):
            valor = "K"    
        elif (self.numero == 1):
            valor = "A"
        else:
            valor = str(self.numero)
        return valor
    
    def obtener_numero(self) -> None:
        return 10 if self.numero > 10 else self.numero
    
    def obtener_nombre_archivo(self)->str:
        return f"/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/juego_21/images/{self.convertir_numero_a_letras()}_de_{self.palo}.png"

if __name__ == '__main__':
    carta: Carta = Carta(11, "treboles")
    carta.imprimir()