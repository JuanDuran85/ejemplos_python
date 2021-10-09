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
            query = "DELETE FROM persona WHERE nombre=%s"
            nombre = ("Odie",)
            cursor.execute(query, nombre)
            registro_eliminado = cursor.rowcount
            print("Registros eleminados en total: {}".format(registro_eliminado))
except Exception as e:
    print("Error al borrar la base de datos: ", e)
finally:
    conexion.close()