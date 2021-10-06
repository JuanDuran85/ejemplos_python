# trabajando con archivos
try:
    archivo = open("archivos.txt", "w", encoding='utf8')
    archivo.write("Agregando información al archivo")
    archivo.write("\n")
    archivo.write("Nueva linea")
except FileNotFoundError:
    print("No se encontro el archivo")
except PermissionError:
    print("No tiene permisos para leer el archivo")
except Exception as e:
    print(e)
finally:
    archivo.close()