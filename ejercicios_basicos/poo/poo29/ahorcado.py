"""_summary_

    Juego del ahorcado mediante clases

"""
import requests

url_api_palabra: str = "https://palabras-aleatorias-public-api.herokuapp.com/random"


class Ahorcado:
    def __init__(self, intentos: int = 5) -> None:
        self.palabra_secreta: str = ""
        self.palabra_usuario: str = ""
        self.intentos: int = intentos
        
    def imprimir_estado(self) -> None:
        print(f"{self.palabra_usuario = }")
        print(f"{self.palabra_secreta = }")
        print(f"Le quedan {self.intentos} intentos")
        
    def buscar_letra(self) -> None:
        ...
        
    def jugar(self) -> None:
        ...
    
    def determinar_si_gano(self) -> None:
        ...
        
    def pedir_letra(self) -> None:
        ...
        
    def quitar_tildes(self, palabra: str) -> str:
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
    
    def traer_palabra(self) -> None:
        respuesta: requests.Response = requests.get(url_api_palabra)
        self.palabra_secreta = self.quitar_tildes(respuesta.json()['body']['Word'])
        self.palabra_usuario = "?" * len(self.palabra_secreta)
        
    def __str__(self) -> str:
        return f"Palabra secreta: {self.palabra_secreta}"
        
if __name__ == "__main__":
    ahorcado: Ahorcado = Ahorcado()
    ahorcado.traer_palabra()
    print(ahorcado)