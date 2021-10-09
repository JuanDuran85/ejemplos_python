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
                UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s;
            """
            valores = ("Eleanora","Wolf","Marcelino19@yahoo.com",7)
            cursor.execute(query, valores)
            resultado = cursor.rowcount
            print(f"Se actualizaron {resultado} registros")
except Exception as e:
    print(e)
finally:
    conexion.close()