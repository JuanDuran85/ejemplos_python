# trabajando con archivos - lectura
try:
    # en windows se debe utilizar \\ para separar carpetas
    archivo = open('C:\\Users\\BC\\Documents\\ejemplos\\ejercicios_python\\archivos.txt', 'r', encoding='utf8')
    # leer algunos caracteres
    print(archivo.read(5))

    # leer lineas completas
    print(archivo.readline())

    # leer todo el archivo o resto de los caracteres
    print(archivo.read())
except Exception as e:
    print(e)

