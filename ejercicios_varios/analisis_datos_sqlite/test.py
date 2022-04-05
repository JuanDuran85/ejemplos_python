"""_summary_

    Realizando test basicos con unittest

"""

import locale
from sqlite3 import Connection
import unittest

from pandas import DataFrame
from vehiculos import borrar_datos, guardar_vehiculos, leer_datos, crear_conexion_bd, crear_tabla_vehiculos, numero_total_vehiculos, precio_total

nombre_fichero: str = "/home/juan/Descargas/programacion/ejemplos_python/ejercicios_varios/analisis_datos_sqlite/test.csv" 

class TestNumeroVechiculos(unittest.TestCase):
    def test(self):
        borrar_datos()
        datos_leidos: DataFrame = leer_datos(nombre_fichero)
        conexion: Connection = crear_conexion_bd()
        crear_tabla_vehiculos(conexion)
        guardar_vehiculos(conexion, datos_leidos)
        numero_vehiculos_total: float = numero_total_vehiculos(conexion)[0][0]
        self.assertEqual(2780, numero_vehiculos_total)
        
class TestPrecioTotalVehiculo(unittest.TestCase):
    def test_two(self):
        borrar_datos()
        datos_leidos: DataFrame = leer_datos(nombre_fichero)
        conexion: Connection = crear_conexion_bd()
        crear_tabla_vehiculos(conexion)
        guardar_vehiculos(conexion, datos_leidos)
        precio_total_vehiculo = locale.currency(precio_total(conexion), grouping=True)
        self.assertEqual('38.997.136,00 €', precio_total_vehiculo)
    
if __name__ == '__main__':
    unittest.main()