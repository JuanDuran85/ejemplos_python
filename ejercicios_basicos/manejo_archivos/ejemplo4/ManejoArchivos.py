# la clase se puede utilizar para menejar recursos
class ManejoArchivos:
    def __init__(self, archivo):
        self.archivo = archivo
    
    def __enter__(self):
        print("Abriendo archivo".center(50, "-"))
        try:
            self.archivo = open(self.archivo, 'r', encoding="utf8")
            return self.archivo
        except Exception:
            print("Error al abrir el archivo")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Cerrando archivo".center(50, "-"))
        if exc_type or exc_value or traceback:
            print("Error en el archivo")
        if self.archivo:
            self.archivo.close()
            print("Archivo cerrado")

# se hereda de la clase object