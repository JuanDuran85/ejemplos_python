"""_summary_

    Juego del ahorcado mediante clases

"""
import requests

url_api_palabra: str = "https://palabras-aleatorias-public-api.herokuapp.com/random"

class Ahorcado:
    def __init__(self, palabra: str = "",intentos: int = 5) -> None:
        self.palabra_secreta: str = palabra.lower() if len(palabra) >= 3 else self.__traer_palabra()
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
    
    def __traer_palabra(self) -> str:
        try:
            respuesta: requests.Response = requests.get(url_api_palabra)
            return self.__quitar_tildes(respuesta.json()['body']['Word'])
        except Exception as e:
            print(f"Error en la API: {e}")
        
    def __str__(self) -> str:
        return f"Palabra secreta: {self.palabra_secreta}"
        
if __name__ == "__main__":
    ahorcado: Ahorcado = Ahorcado()
    ahorcado.jugar()
    