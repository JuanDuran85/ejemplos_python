import os
from dotenv import load_dotenv
from psycopg2 import pool
from logger_base import log
import sys

load_dotenv()

class Conexion:
    __DATABASE = os.getenv("DATABASE")
    __USER = os.getenv("USER")
    __PASSWORD = os.getenv("PASSWORD")
    __HOST = os.getenv("HOST")
    __PORT = os.getenv("PORT")
    __MAX_CONEXIONES = int(os.getenv("MAX_CONEXIONES"))
    __MIN_CONEXIONES = int(os.getenv("MIN_CONEXIONES"))
    __POOL = None

    @classmethod
    def obtener_pool(cls):
        if cls.__POOL is None:
            try:
                cls.__POOL = pool.SimpleConnectionPool(
                    cls.__MIN_CONEXIONES,
                    cls.__MAX_CONEXIONES,
                    database=cls.__DATABASE,
                    user=cls.__USER,
                    password=cls.__PASSWORD,
                    host=cls.__HOST,
                    port=cls.__PORT
                )
                log.debug("Conexión establecida con éxito")
                return cls.__POOL
            except Exception as e:
                log.error("Ocurrio un error en la conexion: {}".format(e))
                sys.exit(1)
        else:
            return cls.__POOL

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug("Conexión obtenida con éxito")
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug("Conexión liberada con éxito: {}".format(conexion))

    @classmethod
    def cerrar_conexion(cls):
        cls.obtener_pool().closeall()
        log.debug("Conexiones cerradas con éxito")

if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    conexion2 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion3)
    Conexion.liberar_conexion(conexion4)
    conexion5 = Conexion.obtener_conexion()