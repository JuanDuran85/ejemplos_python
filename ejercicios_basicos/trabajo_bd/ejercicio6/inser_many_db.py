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
            query = """
            INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)
            """
            valores = (
                ("Odie","Hilll","Golden.Swaniawski@yahoo.com"),
                ("Genevieve","Upton","Arlene_Beatty@hotmail.com"),
                ("Lorenz","Kuhlman","lk@mail.com")
            )
            cursor.executemany(query, valores)
            registros = cursor.rowcount
            print("Se han insertado los datos... {}".format(registros))
except Exception as e:
    print("El error fue: ",e)
finally:
    conexion.close()