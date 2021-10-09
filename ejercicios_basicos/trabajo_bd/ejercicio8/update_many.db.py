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
            query = "UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s;"
            valores = (
                ("Brooklyn", "Wyman", "Abel62@yahoo.com", 1),
                ("Kimberly", "Schmidt", "Mireille38@hotmail.com", 2),
                ("Cecilia", "Schultz", "Stone_Schultz@hotmail.com", 3),
                ("Kamron", "Douglas", "Casimer.Romaguera@gmail.com", 4),
                ("Seamus", "Beatty", "Kacey_Emmerich@hotmail.com", 5),
                ("Jaylen", "Dietrich", "Esther.Dooley@yahoo.com", 6),
            )
            cursor.executemany(query, valores)
            print("Registros actualizados: ", cursor.rowcount)
except Exception as e:
    print("Error: ", e)
finally:
    conexion.close()