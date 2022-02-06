# trabajando con archivos en python

try:
    archivo = open("archivo.txt", "w", encoding="utf8")
    archivo.write("Primera linea agrega al archivo desde python")
    archivo.write("\n")
    archivo.write("Segunda linea agrega al archivo desde python")
    archivo.write("\n")
except Exception as e:
    print("Error al abrir el archivo: {}".format(e))
finally:
    archivo.close()
    print("Se ha cerrado el archivo")