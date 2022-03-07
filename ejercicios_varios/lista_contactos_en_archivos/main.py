import os
from personas import Contacto
from trabajo_archivos import (CARPETA, EXTENSION, buscar_archivo, crear_directorio, leer_archivo, renombrar_archivo, trabajando_en_archivo)


def agregar_contacto() -> None:
    print("Escribe los datos para agregar el contacto")

    nombre_contacto: str = input("Nombre del contacto: \r\n")

    if not buscar_archivo(nombre_contacto):
        telefono_contacto: str = input("Telefono del contacto: \r\n")
        categoria_contacto: str = input("Categoria del contacto: \r\n")

        contacto_agregar: Contacto = Contacto(
            nombre_contacto, telefono_contacto, categoria_contacto)

        contacto: dict = {
            "nombre": contacto_agregar.nombre,
            "telefono": contacto_agregar.telefono,
            "categoria": contacto_agregar.categoria
        }

        trabajando_en_archivo(contacto, 'w')
    else:
        print("Un archivo ya existe con ese nombre")

    app()


def editar_contacto() -> None:
    print("Contactos a Editar \r\n")
    nombre_anterior: str = input("Nombre del contacto a editar: \r\n")

    if buscar_archivo(nombre_anterior):

        nombre_contacto: str = input(
            "Agrega el nuevo nombre del contacto: \r\n")
        renombrar_archivo(nombre_anterior, nombre_contacto)

        telefono_contacto: str = input(
            "Agrega el nuevo Telefono del contacto: \r\n")
        categoria_contacto: str = input(
            "Agrega la nueva Categoria del contacto: \r\n")

        contacto_agregar: Contacto = Contacto(
            nombre_contacto, telefono_contacto, categoria_contacto)

        contacto: dict = {
            "nombre": contacto_agregar.nombre,
            "telefono": contacto_agregar.telefono,
            "categoria": contacto_agregar.categoria
        }

        trabajando_en_archivo(contacto, 'w')
    else:
        print("El contacto no existe.")

    app()


def ver_contacto() -> None:
    archivos: list[str] = os.listdir(CARPETA)
    archivos_txt: list[str] = [i for i in archivos if i.endswith(EXTENSION)]
    print(f"\r\nContactos a mostrar: {len(archivos_txt)}\r\n")
    for archivo in archivos_txt:
        leer_archivo(archivo.replace(EXTENSION, ""))
    app()


def buscar_contacto() -> None:
    print("Buscando contacto...")
    nombre_contacto: str = input("\r\nNombre del contacto a buscar: \r\n")

    if buscar_archivo(nombre_contacto):
        print(f"\r\nContacto encontrado\r\n")
        leer_archivo(nombre_contacto)
    else:
        print("\r\nContacto no encontrado\r\n")

    app()


def eliminar_contacto() -> None:
    print("Eliminando Contactos")
    eliminar_contacto = input("Nombre del contacto a eliminar: \r\n")
    try:
        os.remove(CARPETA+ eliminar_contacto + EXTENSION)
        print("\r\nContacto eliminado correctamente \r\n")
    except Exception as e:
        print(f"\r\nContacto no encontrado\r\n")
        raise e
    app()
    
def app() -> None:

    crear_directorio()
    menu_opciones()

    preguntar: bool = True
    opciones: dict = {
        1: agregar_contacto,
        2: editar_contacto,
        3: ver_contacto,
        4: buscar_contacto,
        5: eliminar_contacto,
        6: salir
    }

    while preguntar:
        try:
            opcion: int = int(input("Selecciona una opcion: \r\n"))
            if (opcion in opciones):
                opciones[opcion]()
                preguntar = False
            else:
                print(f"Opcion ingresada no valida")
        except Exception:
            print("Opcion no valida. Solo deben ser numeros")
        
def salir() -> None:
    print("Saliendo...")
    exit()


def menu_opciones() -> None:
    print("Opciones disponilbes: ")
    print("1. Agregar contacto")
    print("2. Editar contactos")
    print("3. Ver contactos")
    print("4. Buscar contactos")
    print("5. Eliminar contactos")
    print("6. Salir")


if __name__ == '__main__':
    app()
