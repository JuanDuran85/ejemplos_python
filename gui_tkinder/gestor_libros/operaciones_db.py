"""_summary_

    Gestor de libros con Tkinder y SQLite

"""

from sqlite3 import Connection, Cursor, connect

direccion_base_datos: str = "/home/juan/Descargas/programacion/ejemplos_python/gui_tkinder/gestor_libros/libros.db"

def conectar(query: str = "", tipo: str = 'SELECT', values: tuple = ()) -> list:
    try:
        conexion: Connection = connect(direccion_base_datos)
        cursor: Cursor = conexion.cursor()
        if tipo == 'SELECT':
            cursor.execute(query, values)
            resultado_consulta: list = cursor.fetchall()
            return resultado_consulta
        elif tipo == 'CREATE':
            cursor.execute(query)
            conexion.commit()
        else:
            cursor.execute(query, values)
            conexion.commit()
    except Exception as e:
        print(f"Error en conexion a base de datos: {e}")
    finally:
        conexion.close()
 
def crear_tabla() -> None:
    query: str = "CREATE TABLE IF NOT EXISTS libros(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, anio INTEGER, isbn INTEGER)"
    conectar(query, "CREATE")
    
def insertar(titulo: str, autor: str, anio: int, isbn: int) -> None:
    conectar("INSERT INTO libros VALUES (NULL,?, ?, ?, ?)","INSERT" ,(titulo, autor, anio, isbn))
    
def visualizar() -> list:
    return conectar("SELECT * FROM libros", "SELECT")

def buscar(titulo: str = "", autor: str = "", anio: int = 0, isbn: int = 0) -> list:
    return conectar("SELECT * FROM libros WHERE titulo = ? OR autor = ? OR anio = ? OR isbn = ?", "SELECT", (titulo, autor, anio, isbn))

def borrar(id: int) -> None:
    conectar("DELETE FROM libros WHERE id = ?", "DELETE", (id,))
    
def actualizar(id: int, titulo: str = "", autor: str = "", anio: int = 0, isbn: int = 0) -> None:
    conectar("UPDATE libros SET titulo = ?, autor = ?, anio = ?, isbn = ? WHERE id = ?", "UPDATE", (titulo, autor, anio, isbn, id))
    
# pruebas
if __name__ == '__main__':
    crear_tabla()
    insertar("test11","josefa",2002,114)
    result: list = visualizar()
    print(f"Visualizar: {result}")
    result: list = buscar(anio=2000)
    print(f"Buscar: {result}")
    borrar(5)
    result: list = visualizar()
    print(f"Visualizar: {result}")
    actualizar(4,"Petronila","Nuevo Libro",2001,1111)
    result: list = visualizar()
    print(f"Visualizar: {result}")