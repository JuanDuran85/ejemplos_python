import os

CARPETA: str = 'ejercicios_varios/lista_contactos_en_archivos/contactos/'
EXTENSION: str = '.txt'

class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria
        
    def __str__(self):
        return f'{self.nombre} - {self.telefono} - {self.categoria}'
    
def app() -> None:
    
    crear_directorio()
    menu_opciones()
    
    preguntar: bool = True
    opciones: dict = {
        1: agregar_contacto,
        2: editar_contacto,
        3: ver_contacto,
        4: buscar_contacto,
        5: eliminar_contacto
    }
    
    while preguntar:
        opcion: int = int(input("Selecciona una opcion: \r\n"))
        try:
            opciones[opcion]()
            preguntar = False
        except KeyError:
            print("Opcion no valida")

def agregar_contacto() -> None:
    print("Escribe los datos para agregar el contacto")
    nombre_contacto: str = input("Nombre del contacto: \r\n")
    telefono_contacto: str = input("Telefono del contacto: \r\n")
    categoria_contacto: str = input("Categoria del contacto: \r\n")
    
    contacto_agregar: Contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)
    
    contacto: dict = {
        "nombre": contacto_agregar.nombre,
        "telefono": contacto_agregar.telefono,
        "categoria": contacto_agregar.categoria
    }
    
    trabajando_en_archivo(contacto, 'w')
    print(f"Contacto agregado correctamente: {contacto_agregar}")


def trabajando_en_archivo(datos_contacto, operacion_archivo) -> None:
   with open(CARPETA + datos_contacto['nombre'] + EXTENSION, operacion_archivo) as archivo:
        for key, value in datos_contacto.items():
            archivo.write(f"{key}: {value} \r\n")     
            
def editar_contacto() -> None:
    print("Editar contacto")
    
def ver_contacto() -> None:
    print("Ver contacto")
    
def buscar_contacto() -> None:
    print("Buscar contacto")

def eliminar_contacto() -> None:
    print("Eliminar contacto")

def menu_opciones() -> None:
    print("Opciones disponilbes: ")
    print("1. Agregar contacto")
    print("2. Editar contactos")
    print("3. Ver contactos")
    print("4. Buscar contactos")
    print("5. Eliminar contactos")

def crear_directorio() -> None:
    if not os.path.exists(CARPETA):
        os.mkdir(CARPETA)
    else:
        print('El directorio ya existe')
    
if __name__ == '__main__':
    app()