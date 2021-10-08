# conextando a base de datos con with

import psycopg2

conexion = psycopg2.connect(
    database="test_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sql_query = "SELECT * FROM persona WHERE nombre = %s"
            nombre = input("Ingrese el nombre de la persona: ")
            cursor.execute(sql_query, (nombre,))
            registro = cursor.fetchone()
            print(registro)
except Exception as e:
    print(e)
finally:
    conexion.close()

