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
    def get_pool(cls):
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
                log.debug(f"Pool disponible: {cls.__POOL}")
                return cls.__POOL
            except Exception as e:
                log.error(f"Error al crear la conexión: {e}")
                sys.exit(1)
        else:
            return cls.__POOL

    @classmethod
    def get_connection(cls):
        conexion = cls.get_pool().getconn()
        log.debug(f"Conexiones abiertas: {conexion}")
        return conexion

    @classmethod
    def free_connection(cls, conexion):
        cls.get_pool().putconn(conexion)
        log.debug(f"Conexiones liberada: {conexion}")

    @classmethod
    def close_connection(cls):
        cls.get_pool().closeall()
        log.debug(f"Conexiones cerrada: {cls.__POOL}")


if __name__ == '__main__':
    conexion1 = Conexion.get_connection()
    conexion2 = Conexion.get_connection()
    Conexion.free_connection(conexion1)
    conexion3 = Conexion.get_connection()
    conexion4 = Conexion.get_connection()
    Conexion.free_connection(conexion3)
    Conexion.free_connection(conexion4)
    conexion5 = Conexion.get_connection()