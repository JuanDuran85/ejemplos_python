"""
 context manager para manejar el pool de conexiones
 resouces o Context Manager
"""

from conexion import Conexion
from logger_base import log
class CursorPool:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        log.debug("Inicio de la clase cursor con el metodo with __enter__")
        self.__conexion = Conexion.obtener_conexion()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug("Fin de la clase cursor con el metodo with __exit__")
        if exc_val:
            self.__conexion.rollback()
            log.error("Error en la clase cursor con el metodo with __exit__: {} - {} - {}".format(exc_val, exc_type, exc_tb))
        else:
            self.__conexion.commit()
            log.debug("Conexion finalizada con el metodo with __exit__")
        self.__cursor.close()
        Conexion.liberar_conexion(self.__conexion)

if __name__ == '__main__':
    with CursorPool() as cursor:
        cursor.execute("SELECT * FROM persona")
        for fila in cursor:
            print(fila)