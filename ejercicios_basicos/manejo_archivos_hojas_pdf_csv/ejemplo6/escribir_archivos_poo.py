"""_summary_

    Manejo de achivos "Escritura" mediante clases POO

"""

from io import TextIOWrapper

class EscritorDeArchivos:
    
    def __init__(self, archivo: str, agregar_al_final: bool = False) -> None:
        self.abrir(archivo, agregar_al_final)
    
    def abrir(self, archivo: str, agregar_al_final: bool = False) -> None:
        try:
            modo: str = 'a' if agregar_al_final else 'w'
            self.escritor: TextIOWrapper = open(archivo, modo)
        except Exception as e:
            print(f"Error en archivo: {e}")
        
    def cerrar(self) -> None:
        self.escritor.close()
        
    def escribir(self, texto: str) -> bool:
        datos_escritos: bool = False
        if (not self.escritor.closed):
            self.escritor.write(texto)
            datos_escritos = True
        return datos_escritos
        
def main():
    escritor: EscritorDeArchivos = EscritorDeArchivos("Prueba.txt", True)
    escritor.escribir("Programando con Python\n")
    escritor.cerrar()
    
if __name__ == "__main__":
    main()