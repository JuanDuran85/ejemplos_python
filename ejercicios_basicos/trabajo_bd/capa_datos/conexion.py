import os
from dotenv import load_dotenv
import psycopg2 as db
from logger_base import log
import sys

load_dotenv()

class Conexion:
    __DATABASE = os.getenv("DATABASE")
    __USER = os.getenv("USER")
    __PASSWORD = os.getenv("PASSWORD")
    __HOST = os.getenv("HOST")
    __PORT = os.getenv("PORT")
    __conexion = None
    __cursor = None

    @classmethod
    def obtener_conexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(
                    database=cls.__DATABASE,
                    user=cls.__USER,
                    password=cls.__PASSWORD,
                    host=cls.__HOST,
                    port=cls.__PORT
                )
                log.debug("Conexión establecida: {}".format(cls.__conexion))
                return cls.__conexion
            
            except Exception as e:
                log.error("Ocurrio un error en la conexion: {}".format(e))
                sys.exit(1)
        else:
            return cls.__conexion

    @classmethod
    def obtener_cursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.__conexion.cursor()
                log.debug("Cursor establecido: {}".format(cls.__cursor))
                return cls.__cursor
            
            except Exception as e:
                log.error("Ocurrio un error en el cursor: {}".format(e))
                sys.exit(1)
        else:
            return cls.__cursor

    @classmethod
    def cerrar(cls):
        cls.__cursor.close()
        cls.__conexion.close()

if __name__ == '__main__':
    conexion = Conexion.obtener_conexion()
    cursor = Conexion.obtener_cursor()
    cursor.execute("SELECT * FROM persona")
    print(cursor.fetchall())
    Conexion.cerrar()