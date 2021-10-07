from dominio.Pelicula import Pelicula
from servicio.CatalogoPelicula import CatalogoPelicula

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
        if opcion == 1:
            print("Añadir película".center(50, "-"))
            nombre = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre)
            CatalogoPelicula.agregar_pelicula(pelicula)
            print("Película agregada".center(50, "-"))
        elif opcion == 2:
            CatalogoPelicula.listar_pelicula()
        elif opcion == 3:
            print("Buscando una pelicula".center(50, "-"))
            nombre = input("Ingrese el nombre de la película: ")
            CatalogoPelicula.buscar_pelicula(nombre)
        elif opcion == 4:
            print("Borrar archivo de películas".center(50, "-"))
            CatalogoPelicula.eliminar_pelicula()
            print("Archivo de películas borrado".center(50, "-"))
        elif opcion == 5:
            break
    except Exception as e:
        print(e)
        print("Ingrese una opción válida")
        opcion = None

print("Gracias por usar el programa")
exit()
