"""_summary_

    Manejo de achivos "Lectura" mediante clases POO

"""

class LectorDeArchvio:
    
    def __init__(self, nombre_archivo: str) -> None:
        self.abrir(nombre_archivo)
        
    def abrir(self, nombre_archivo: str) -> None:
        try:
            self.lector = open(nombre_archivo, 'r', encoding='utf8')
            self.esta_abierto: bool = True
        except FileNotFoundError as e:
            self.lector = None
            self.esta_abierto = False
            print(f"Error en archivo: {e}")
            
    def cerrar(self) -> None:
        if self.esta_abierto:
            self.lector.close()
            self.esta_abierto = False
        else:
            print("El archivo no esta abierto")
        
    def leer_linea(self) -> str:
        linea: str = ""
        if self.esta_abierto and not self.lector.closed:
            linea = self.lector.readline()
        return linea
    
    def leer_lineas(self) -> list:
        archivo: list = []
        if self.esta_abierto and not self.lector.closed:
            archivo = self.lector.readlines()
        return archivo
            
    def leer_archivo(self) -> str:
        archivo: str = ""
        if self.esta_abierto and not self.lector.closed:
            linea: str = self.lector.readline()
            while(len(linea) != 0):
                archivo += linea
                linea = self.lector.readline()
        return archivo
    
def main():
    lector: LectorDeArchvio = LectorDeArchvio("Prueba.txt")
    print(lector.leer_archivo())
    lector.cerrar()
    
if __name__ == "__main__":
    main()