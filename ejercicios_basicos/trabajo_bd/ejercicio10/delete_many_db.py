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
            query = "DELETE FROM persona WHERE id_persona IN %s"
            entrada = input("Ingrese el id de la(s) persona(s) a eliminar separados por coma: ")
            id_personas = (tuple(entrada.split(",")),)
            cursor.execute(query, id_personas)
            resultado = cursor.rowcount
            print(f"Se eliminaron {resultado} registros")
except Exception as e:
    print("Error: ", e)
finally:
    conexion.close()