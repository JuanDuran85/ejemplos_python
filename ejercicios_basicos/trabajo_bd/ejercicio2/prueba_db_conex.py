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
            sql_query = "SELECT * FROM persona"
            cursor.execute(sql_query)
            registro = cursor.fetchall()
            print(registro)
except Exception as e:
    print(e)
finally:
    conexion.close()

