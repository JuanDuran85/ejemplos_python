"""_summary_

    Juego del ahorcado mediante clases

"""

import random
from leer_archivo_poo import LectorDeArchvio

class Ahorcado:
    def __init__(self, palabra: str = "",intentos: int = 5) -> None:
        self.palabra_secreta: str = self.__quitar_tildes(palabra.lower())
        self.palabra_usuario: str = "?" * len(self.palabra_secreta)
        self.intentos: int = intentos
        
    def imprimir_estado(self) -> None:
        print(f"{self.palabra_usuario = }")
        print(f"{self.palabra_secreta = }")
        print(f"Le quedan {self.intentos} intentos")
        
    def buscar_letra(self, letra: str) -> int:
        numero_veces: int = 0
        for i in range(len(self.palabra_secreta)):
            if (self.palabra_secreta[i] == letra):
                numero_veces += 1
                self.palabra_usuario = self.palabra_usuario[:i] + letra + self.palabra_usuario[i+1:]
        return numero_veces
        
    def jugar(self) -> None:
        while(not self.determinar_si_gano() and self.intentos > 0):
            self.imprimir_estado()
            letra: str = self.pedir_letra()
            numero_veces: int = self.buscar_letra(letra)
            if (numero_veces == 0):
                self.intentos -= 1
        if (self.intentos == 0):
            print("Perdiste")
        else:
            print("Ganaste")
            
    
    def determinar_si_gano(self) -> bool:
        return self.palabra_usuario.find("?") == -1
        
    def pedir_letra(self) -> str:
        letra: str = self.__quitar_tildes(input("Ingrese una letra: "))
        return letra
        
    def __quitar_tildes(self, palabra: str) -> str:
        palabra = palabra.lower()
        acentos: dict = {
            'á':'a',
            'é':'e',
            'í':'i',
            'ó':'o',
            'ú':'u',
        }
        
        for vocal in acentos:
            if vocal in palabra:
                palabra = palabra.replace(vocal, acentos[vocal])
        return palabra        
    
    def __str__(self) -> str:
        return f"Palabra secreta: {self.palabra_secreta}"

def main() -> None:
    
    lector: LectorDeArchvio = LectorDeArchvio("/home/juan/Descargas/programacion/ejemplos_python/ejercicios_basicos/poo/poo30/palabras.txt")
    lista_palabras = lector.leer_lineas()
    aleatorio_numero = int(random.random() * len(lista_palabras))
    ahorcado: Ahorcado = Ahorcado(lista_palabras[aleatorio_numero].replace('\n', ''))
    ahorcado.jugar()
    
if __name__ == "__main__":
    main()