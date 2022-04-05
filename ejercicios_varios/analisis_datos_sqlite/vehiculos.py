"""_summary_

    Trabajando con SQLite, pandas, zipfile y sys para descompimir un fichero zip y leer los datos de un fichero csv, analizar con pandas.

"""

import sys
from sqlite3 import Connection, Cursor, connect
from zipfile import ZipFile

from pandas import DataFrame, read_csv


# funcion para descompimir fichero zip
def descomprimir_fichero(nombre: str) -> None:
    """_summary_
        Funcion para descompimir fichero zip
    """
    with ZipFile(nombre, 'r') as fichero_zip:
        print(fichero_zip)
        fichero_zip.extractall('/home/juan/Descargas/programacion/ejemplos_python/ejercicios_varios/analisis_datos_sqlite')
        
# funcion para leer fichero csv
def leer_datos(nombre: str) -> DataFrame:
    """_summary_
        Funcion para leer datos de un fichero csv
    """
    data_frame_datos: DataFrame = read_csv(nombre, sep=';')
    return data_frame_datos

# funcion para conectar a la base de datos sqlite
def crear_conexion_bd() -> Connection:
    """_summary_
        Funcion para conectar a la base de datos sqlite
    """
    try:
        conexion_db: Connection = connect('/home/juan/Descargas/programacion/ejemplos_python/ejercicios_varios/analisis_datos_sqlite/vehiculos.db')
        return conexion_db
    except Exception as e:
        print(f"Error: {e}")
        
def crear_tabla_vehiculos(conexion: Connection) -> None:
    """_summary_
        Funcion para crear la tabla principal en la base de datos sqlite
    """
    cursor: Cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos (marca Text, modelo Text, combustible Text, transmision Text, estado Text, matriculacion Text, kilometraje Integer, potencia Real, precio Real)""")
    conexion.commit()
    
def guardar_vehiculos(conexion: Connection, datos: DataFrame) -> None:
    """_summary_
        Funcion para guardar los datos en la tabla principal en la base de datos sqlite
    """
    for filas in datos.itertuples():
        marca = filas[1]
        modelo = filas[2]
        combustible = filas[3]
        transmision = filas[4]
        estado = filas[5]
        matriculacion = filas[6]
        kilometraje = filas[7]
        potencia = filas[8]
        precio = filas[9]
    
        vehiculo: tuple = (marca, modelo, combustible, transmision, estado, matriculacion, kilometraje, potencia, precio)

        
    cursor: Cursor = conexion.cursor()
    cursor.execute("""""")




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error. Numero de parametros incorrectos")
    else:
        nombre_archivo: str = sys.argv[1]
        descomprimir_fichero(nombre_archivo)
        datos_leidos: DataFrame = leer_datos('/home/juan/Descargas/programacion/ejemplos_python/ejercicios_varios/analisis_datos_sqlite/coches.csv')
        conexion: Connection = crear_conexion_bd()
        
        # crear tabla de vehiculos
        crear_tabla_vehiculos(conexion)
        
        # grabando vehiculos en la base de datos
        guardar_vehiculos(conexion, datos_leidos)
        
