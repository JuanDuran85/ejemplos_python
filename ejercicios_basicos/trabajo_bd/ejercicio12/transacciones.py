import psycopg2 as db

conexion = db.connect(
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
            values = ('Savanah','Runolfsdot','sr@yahoo.com')
            cursor.execute(query, values) 

            query = """
                UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s
            """
            values = ('Modificado','Macejkovic','Larrysss34@gmail.com',10)
            cursor.execute(query, values)
except Exception as e:
    print("Error: ", e)
finally:
    print("Modificada la BD, commit activo")
    cursor.close()
    conexion.close()