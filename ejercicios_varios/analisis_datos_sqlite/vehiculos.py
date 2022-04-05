"""_summary_

    Trabajando con SQLite, pandas, zipfile y sys para descompimir un fichero zip y leer los datos de un fichero csv, analizar con pandas.

"""

from os import remove
import sys
from sqlite3 import Connection, Cursor, connect
from zipfile import ZipFile
import locale

from pandas import DataFrame, options, read_csv

locale.setlocale(locale.LC_MONETARY, 'es_ES.UTF-8')

# funcion para borrar los datos
def borrar_datos() -> None:
    """_summary_
        Funcion para borrar datos de la DB
    """
    try:
        remove('/home/juan/Descargas/programacion/ejemplos_python/ejercicios_varios/analisis_datos_sqlite/vehiculos.db')
    except FileNotFoundError:
        print("No existe la DB")

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

# funcion para crear la tabla principal para la base de datos sqlite        
def crear_tabla_vehiculos(conexion: Connection) -> None:
    """_summary_
        Funcion para crear la tabla principal en la base de datos sqlite
    """
    cursor: Cursor = conexion.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS vehiculos (id INTEGER PRIMARY KEY AUTOINCREMENT, marca Text, modelo Text, combustible Text, transmision Text, estado Text, matriculacion Text, kilometraje Integer, potencia Real, precio Real)""")
    conexion.commit()
    
def consultar_vehiculos(conexion: Connection) -> None:
    cursor: Cursor = conexion.cursor()
    cursor.execute("""SELECT * FROM vehiculos limit 22""")
    filas: list = cursor.fetchall()
    for i,fila in enumerate(filas):
        print(f"{i+1} - {fila}")
        
def numero_total_vehiculos(conexion: Connection) -> list:
    cursor: Cursor = conexion.cursor()
    cursor.execute("""SELECT count(*) FROM vehiculos""")
    numero_vehiculos: list = cursor.fetchall()
    return numero_vehiculos

def precio_total(conexion: Connection) -> float:
    cursor: Cursor = conexion.cursor()
    cursor.execute("""SELECT sum(precio) FROM vehiculos""")
    precio_total: list = cursor.fetchall()
    return precio_total[0][0]

def vechiculo_economico(conexion: Connection) -> list:
    cursor: Cursor = conexion.cursor()
    cursor.execute("SELECT * FROM vehiculos WHERE precio = (SELECT min(precio) FROM vehiculos)")
    return cursor.fetchall()

def precio_medio_marca(conexion: Connection) -> list:
    cursor: Cursor = conexion.cursor()
    cursor.execute("""SELECT marca, avg(precio) FROM vehiculos GROUP BY marca""")
    return cursor.fetchall()
    
# funcion para insertar vehiculos en la base de datos sqlite
def insertar_vehiculo(conexion: Connection, vehiculo: tuple) -> None:
    """_summary_
        funcion para insertar vehiculos en la base de datos sqlite
    """
    cursor: Cursor = conexion.cursor()
    cursor.execute("""INSERT OR IGNORE INTO vehiculos(marca, modelo, combustible, transmision, estado, matriculacion, kilometraje, potencia, precio) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", vehiculo)
    conexion.commit()

# funcion para guardar los datos en la tabla principal en la base de datos sqlite
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
        insertar_vehiculo(conexion, vehiculo)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error. Numero de parametros incorrectos")
    else:
        borrar_datos()
        nombre_archivo: str = sys.argv[1]
        descomprimir_fichero(nombre_archivo)
        datos_leidos: DataFrame = leer_datos('/home/juan/Descargas/programacion/ejemplos_python/ejercicios_varios/analisis_datos_sqlite/coches.csv')
        conexion: Connection = crear_conexion_bd()
        
        # crear tabla de vehiculos
        crear_tabla_vehiculos(conexion)
        
        # grabando vehiculos en la base de datos
        guardar_vehiculos(conexion, datos_leidos)
        
        # consultando datos de la BD
        print("\nConsultando datos de la BD - 20 primeros registros")
        consultar_vehiculos(conexion)
        
        # calcular el numero total de vechiculos en la DB
        print(f"Numero total de vehiculos: {numero_total_vehiculos(conexion)[0][0]}")
        
        # calcular el precio total de vechiculos
        dinero = '{:,.2f}'.format(precio_total(conexion)).replace(',', '.')
        print(dinero)
        print(f"Precio total de vehiculos: {locale.currency(precio_total(conexion), grouping=True)}")
        
        # marca del vehiculo mas economico
        for i,vehiculo in enumerate(vechiculo_economico(conexion)):
            print(f"""Vehiculo mas economico {i+1}: 
                  Marca: {vehiculo[1]}
                  Modelo: {vehiculo[2]}
                  Precio: {locale.currency(vehiculo[9], grouping=True)}
                  """)
            
        # precio medio por marca
        dataframe_marcas_precio: DataFrame = DataFrame(precio_medio_marca(conexion), columns=['Marca', 'Precio'])
        dataframe_marcas_precio['Precio'] = dataframe_marcas_precio['Precio'].map('{:,.2f}€'.format)
        print(dataframe_marcas_precio)
