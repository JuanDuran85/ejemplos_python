class Pelicula:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return "Pelicula: {}".format(self.__nombre)

if __name__ == '__main__':
    peli = Pelicula('El señor de los anillos')
    print(peli)