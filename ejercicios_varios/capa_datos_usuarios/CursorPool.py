
from logger_base import log
from Conexion import Conexion

class CursorPool:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        log.debug('__enter__')
        self.__conexion = Conexion.get_connection()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('__exit__')
        if exc_val:
            self.__conexion.rollback()
            log.error(f"Error: {exc_val}, {exc_tb}, {exc_type}")
        else:    
            self.__conexion.commit()
            log.debug('Commit realizado')
        
        self.__cursor.close()
        Conexion.free_connection(self.__conexion)

if __name__ == "__main__":
    with CursorPool() as cursor:
        cursor.execute("SELECT * FROM usuario")
        for fila in cursor:
            print(fila)
    