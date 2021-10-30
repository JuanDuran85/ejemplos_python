
from UsuarioDAO import UsuarioDAO
from Usuarios import Usuario
from logger_base import log

def crear_usuario():
    """
    Crea un usuario en el sistema
    """
    log.debug("Creando usuario")
    username = input("Ingrese el nombre del usuario a crear: ")
    password = input("Ingrese la contraseña del usuario: ")
    usuario = Usuario(id_usuario=None, username=username, password=password)
    usuario_creado = UsuarioDAO().insertar(usuario)
    log.debug(f"Usuario creado: {usuario_creado}")

def mostrar_usuario():
    """
    Mostrando usuarios del sistema
    """
    log.debug("Mostrando usuarios")
    usuarios = UsuarioDAO().seleccionar()
    for usuario in usuarios:
        print(usuario)

def actualizar_usuario():
    """
    Actualizar usuario
    """
    log.debug("Actualizando usuario")
    id_usuario = int(input("Ingrese el id del usuario a actualizar: "))
    username = input("Ingrese el nombre del usuario a actualizar: ")
    password = input("Ingrese la contraseña del usuario a actualizar: ")
    usuario = Usuario(id_usuario, username, password)
    usuario_actualizado = UsuarioDAO().actualizar(usuario)
    log.debug(f"Usuario actualizado: {usuario_actualizado}")

def eliminar_usuario():
    """
    Eliminar usuario
    """
    log.debug("Eliminando usuario")
    id_usuario = int(input("Ingrese el id del usuario a eliminar: "))
    username = input("Ingrese el nombre del usuario a eliminar: ")
    usuario = Usuario(id_usuario, username)
    usuario_eliminado = UsuarioDAO().eliminar(usuario)
    log.debug(f"Usuario eliminado: {usuario_eliminado}")

def salida():
    print("Saliendo del programa".center(50, "-"))
    exit()


opciones = {
    1: crear_usuario,
    2: mostrar_usuario,
    3: actualizar_usuario,
    4: eliminar_usuario,
    5: salida
}

opcion = None

while opcion != 5:
    try:
        print("\n ")
        print("Menú de selección: ".center(50, "-"))
        print("1. Crear Usuario")
        print("2. Mostrar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        print("")

        opcion = int(input("Ingrese una opción: "))
        opciones[opcion]()

    except Exception as e:
        print(e)
        print("Ingrese una opción válida")
        opcion = None