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
            sql_query = """

                INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)
            """
            valores = ('Pearl', 'Hamill', 'Christ.Hayes@yahoo.com')
            cursor.execute(sql_query, valores)
            # se ejecuta el commit patserior a la insercion en el caso de no trabajar con with
            # conexion.commit()
            registros_modificados = cursor.rowcount
            print("Se insertaron: {} registros en la base de datos".format(registros_modificados))
except Exception as e:
    print("Error: ", e)
finally:
    conexion.close()