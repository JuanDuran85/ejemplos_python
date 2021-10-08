from dominio.Pelicula import Pelicula
from servicio.CatalogoPelicula import CatalogoPelicula

def agregando_pelicula():
    print("Añadir película".center(50, "-"))    
    nombre = input("Ingrese el nombre de la película: ")
    pelicula = Pelicula(nombre)
    CatalogoPelicula.agregar_pelicula(pelicula)
    print("Película agregada".center(50, "-"))

def buscando_pelicula():
    encontrado = ''
    print("Buscando una pelicula".center(50, "-"))
    nombre = input("Ingrese el nombre de la película: ")
    encontrado = CatalogoPelicula.buscar_pelicula(nombre)
    if encontrado:
        print("Película encontrada".center(50, "-"))
        print(encontrado)
    else:
        print("Película no encontrada".center(50, "-"))
        
def salida():
    print("Saliendo del programa".center(50, "-"))
    exit()

opciones = {
    1: agregando_pelicula,
    2: CatalogoPelicula.listar_pelicula,
    3: CatalogoPelicula.eliminar_pelicula,
    4: buscando_pelicula,
    5: salida
}

opcion = None

while opcion != 5:
    try:
        print("\n ")
        print("Menú de selección: ".center(50, "-"))
        print("1. Añadir película")
        print("2. Listar películas")
        print("3. Borrar archivo de películas")
        print("4. Buscar película")
        print("5. Salir")
        print("")

        opcion = int(input("Ingrese una opción: "))
        opciones[opcion]()

    except Exception as e:
        print(e)
        print("Ingrese una opción válida")
        opcion = None