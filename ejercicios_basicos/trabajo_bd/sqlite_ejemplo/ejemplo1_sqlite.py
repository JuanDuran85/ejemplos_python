"""_summary_

    Tranbajando con SQLite desde Python

"""

from sqlite3 import Cursor, connect, Connection

try:
    conexion: Connection = connect("basededatos1.db")

    cursor: Cursor = conexion.cursor()
    cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido TEXT, edad INTEGER)")

    conexion.commit()

except Exception as e:
    print(e)
finally:
    conexion.close()
    print("Se ha cerrado la conexion")
