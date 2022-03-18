"""_summary_

    Tranbajando con SQLite desde Python

"""

from sqlite3 import Cursor, connect, Connection

try:
    # conectando o creando la base de datos
    conexion: Connection = connect("basededatos1.db")
    cursor: Cursor = conexion.cursor()
    # creando tabla
    cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido TEXT, edad INTEGER)")
    # insertando registros
    cursor.execute("INSERT INTO PERSONAS VALUES ('Juan', 'Perez', 17), ('Pedro', 'Gomez', 33)")
    
    lista_personas: list = [("Maria", "Gomez", 12), ("Ana", "Rodriguez", 25), ("Josefa", "Sipes", 37)]
    # insertando registros 
    cursor.executemany("INSERT INTO PERSONAS VALUES (?, ?, ?)", lista_personas)
    
    # consultar datos
    cursor.execute("SELECT * FROM PERSONAS")
    personas: list = cursor.fetchall()
    print(f"{personas = }")
    
    # consultar datos con where
    cursor.execute("SELECT * FROM PERSONAS WHERE edad > 25")
    personas: list = cursor.fetchall()
    print(f"{personas = }")
    
    # consultar y ordenar datos
    cursor.execute("SELECT * FROM PERSONAS ORDER BY edad DESC")
    personas: list = cursor.fetchall()
    print(f"{personas = }")

    # borrar datos
    cursor.execute("DELETE FROM PERSONAS WHERE edad > 35")

    # actualizar datos
    cursor.execute("UPDATE PERSONAS SET edad = edad + 1 WHERE edad > 21")
    
    # consultar datos
    cursor.execute("SELECT * FROM PERSONAS")
    personas: list = cursor.fetchall()
    print(f"{personas = }")

    # se guardan los cambios en la base de datos creada
    conexion.commit()


except Exception as e:
    print(e)
finally:
    conexion.close()
    print("Se ha cerrado la conexion")
