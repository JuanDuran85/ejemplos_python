import os
CARPETA: str = 'ejercicios_varios/lista_contactos_en_archivos/contactos/'
EXTENSION: str = '.txt'

def trabajando_en_archivo(datos_contacto: dict, operacion_archivo: str) -> None:
    with open(CARPETA + datos_contacto['nombre'] + EXTENSION, operacion_archivo) as archivo:
        for key, value in datos_contacto.items():
            archivo.write(f"{key}: {value} \r\n")
    print(f"Contacto agregado correctamente: {datos_contacto}")
    
def buscar_archivo(nombre_contacto: str) -> bool:
    return os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

def crear_directorio() -> None:
    if not os.path.exists(CARPETA):
        os.mkdir(CARPETA)
    else:
        print('El directorio ya existe')
        
def renombrar_archivo(nombre_anterior: str, nombre_contacto: str) -> None:
    os.rename(CARPETA + nombre_anterior + EXTENSION,
                  CARPETA + nombre_contacto + EXTENSION)
    
def leer_archivo(nombre: str) -> None:
    with open(CARPETA + nombre + EXTENSION, 'r') as archivo:
            print(archivo.read())