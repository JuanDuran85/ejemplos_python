import os

class CatalogoPelicula:

    ruta_archivo = 'catalogo_peliculas.txt'

    def __init__(self, pelicula):
        self.pelicula = pelicula

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(pelicula.nombre + '\n')
            print("Pelicula agregada")

    @classmethod
    def listar_pelicula(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print("Catálogo de Peliculas".center(50, '-'))
            print(archivo.read())

    @classmethod
    def buscar_pelicula(cls, titulo):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            for linea in archivo:
                if linea.startswith(titulo):
                    print("pelicula encontrada: {}".format(linea))
                else:
                    print("pelicula no encontrada")
    
    @classmethod
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivo)
        print("Archivo eliminado desde: {}".format(cls.ruta_archivo))