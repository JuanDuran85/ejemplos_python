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
            log.debug("Seleccionando todos los usuarios")
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            log.debug(f"Numero de registros encontrados en total: {len(registros)}")
            log.debug(f"Registros encontrados: {registros}")
            usuarios = []
            for registro in registros:
                new_usuario = Usuario(*registro)
                usuarios.append(new_usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f"Insertando un nuevo usuario: {usuario}")
            cursor.execute(cls.__INSERTAR, (usuario.username, usuario.password))
            registros = cursor.rowcount
            log.debug(f"Numero de registros insertados: {registros}")
            return registros

    @classmethod
    def actualizar(cls, usuario):
        with CursorPool() as cursor:
            log.debug(f"Actualizando un usuario: {usuario}")
            cursor.execute(cls.__ACTUALIZAR, (usuario.username, usuario.password, usuario.id_usuario))
            registros = cursor.rowcount
            log.debug(f"Numero de registros actualizados: {registros}")
            return registros

    @classmethod
    def eliminar(cls, id):
        with CursorPool() as cursor:
            log.debug(f"Eliminando el usuario: {id}")
            cursor.execute(cls.__ELIMINAR, (id,))
            registros = cursor.rowcount
            log.debug(f"Numero de registros eliminados: {registros}")
            return registros

if __name__ == '__main__':
    usuarios = UsuarioDAO.seleccionar()
    print(usuarios)
    ''' usuario = Usuario(username="juan", password="1234")
    resultado = UsuarioDAO.insertar(usuario)
    print(resultado) '''
    usuario = Usuario(id_usuario=1, username="pepe", password="1234")
    resultado = UsuarioDAO.actualizar(usuario)