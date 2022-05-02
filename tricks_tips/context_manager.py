"""_summary_

    Context Manager - With -
    
    1. Implementando el protocolo con las funciones (__enter__, __exit__)
    2. Utilizando la libreria de contextlib

"""

from contextlib import contextmanager
from io import TextIOWrapper
from typing import Generator


print("\n# Context Manager - With -")

#-----------------------------------------------------------------------
# opción 1
class ManejoArchivo:
    
    def __init__(self, nombre_archivo: str) -> None:
        self.nombre_archivo: str = nombre_archivo
        
    def __enter__(self)-> TextIOWrapper:
        self.archivo: TextIOWrapper = open(self.nombre_archivo, "w")
        return self.archivo
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        if self.archivo:
            self.archivo.close()
#--------------------------------------------------------------------------------
#opcion 2

# este metodo es un generador, en primer lugar adquiere el recurso posteriormente suspende temporalmente la ejecucion al utilizar yield. Cuando termina de ser utilizado el metodo, regresa a la ejecucion y cierra el recurso 
@contextmanager
def manejador_archivo(nombre_archivo: str) -> Generator[TextIOWrapper, None, None]:    
    try:
        archivo: TextIOWrapper = open(nombre_archivo, "w")
        yield archivo
    except Exception as e:
        print(e)
    finally:
        archivo.close()
        print("Se cierra el archivo")
            
#-------------------------------------------------------------------------------- 

# ejercicio de identador

class Identador:
    def __init__(self) -> None:
        self.nivel: int = 0

    def __enter__(self):
        self.nivel += 1
        print(f"Nivel: {self.nivel}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.nivel -= 1
    
    def imprimir(self, texto: str):
        print('  '*self.nivel + texto)
        
# ejercicio de identador con la libreria contextlib
class IdentadorDos:
    def __init__(self) -> None:
        self.nivel: int = 0
        
    @contextmanager
    def identador(self) -> Generator[None, None, None]:
        try:
            self.nivel += 1
            yield self
        except Exception as e:
            print(e)
            raise e
        finally:
            self.nivel -= 1
        
    def imprimir(self, texto: str) -> None:
        print('   '*self.nivel + texto)
        
              
#--------------------------------------------------------------------------------            
if __name__ == "__main__":
    # prueba opcion 1
    with ManejoArchivo("/home/juan/Descargas/programacion/ejemplos_python/Prueba.txt") as archivo:
        archivo.write("Nuevo mensaje desde ManejoArchivo")
        print("Mensaje escrito en el archivo")
    
    # prueba opcion 2
    with manejador_archivo("/home/juan/Descargas/programacion/ejemplos_python/Prueba.txt") as archivo_dos:
        archivo_dos.write("Nuevo mensaje desde manejador_archivo")
        archivo_dos.write("\nNuevo mensaje desde manejador_archivo")
        print("Mensaje escrito en el archivo")
        
    # prueba identador
    with Identador() as identador:
        identador.imprimir("Nuevo texto primer nivel")
        with identador:
            identador.imprimir("Nuevo texto segundo nivel")
            with identador:
                identador.imprimir("Nuevo texto tercer nivel")
                
    # prueba identador con la libreria contextlib
    print("\nPrueba identador con la libreria contextlib")
    objetos_iterador: IdentadorDos = IdentadorDos()
    with objetos_iterador.identador():
        objetos_iterador.imprimir("Mensaje en el primer nivel")
        with objetos_iterador.identador():
            objetos_iterador.imprimir("Mensaje en el segundo nivel")
            with objetos_iterador.identador():
                objetos_iterador.imprimir("Mensaje en el tercer nivel")