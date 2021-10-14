from Usuarios import Usuario
from logger_base import log
from CursorPool import CursorPool

class UsuarioDAO:
    __SELECCIONAR = "SELECT * FROM usuario ORDER BY id_usuario"
    __INSERTAR = "INSERT INTO usuario (username, password) VALUES (%s, %s)"
    __ACTUALIZAR = "UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s"
    __ELIMINAR = "DELETE FROM usuario WHERE id_usuario = %s"

    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            log.debug(f"Registros encontrados: {registros}")
            usuarios = []
            for registro in registros:
                usuario = Usuario(*registro)
                usuarios.append(usuario)
            return usuarios

if __name__ == '__main__':
    usuarios = UsuarioDAO.seleccionar()
    print(usuarios)