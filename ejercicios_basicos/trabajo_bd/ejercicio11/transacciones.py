import psycopg2 as db

conexion = db.connect(
    database="test_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

try:
    # quitamos el autocommit para que no se ejecuten las transacciones
    conexion.autocommit = False
    cursor = conexion.cursor()
    query = """
        INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)
    """
    values = ('Savanah','Runolfsdot','sr@yahoo.com')
    cursor.execute(query, values) 

    query = """
        UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s
    """
    values = ('Modificado','Macejkovicks','Larrysss34@gmail.com',13)
    cursor.execute(query, values)

    conexion.commit()
    print("Modificada la BD, commit activo")
except Exception as e:
    conexion.rollback()
    print("Error: ", e)
finally:
    cursor.close()
    conexion.close()