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
            #sql_query = "SELECT * FROM persona WHERE id_persona IN(2,4)"
            sql_query = "SELECT * FROM persona WHERE id_persona IN %s"
            #id_personas = ((1,6),)
            entrada = input("Ingresa los id\' a buscar separados por comas: ")
            id_personas = (tuple(entrada.split(',')),)
            cursor.execute(sql_query,id_personas)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(e)
finally:
    conexion.close()

