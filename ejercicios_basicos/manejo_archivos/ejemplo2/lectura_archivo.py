# trabajando con archivos - lectura
try:
    archivo = open('archivos.txt', 'r', encoding='utf8')
    # leer algunos caracteres
    print(archivo.read(5))

    # leer lineas completas
    print(archivo.readline())

    # leer todo el archivo o resto de los caracteres
    print(archivo.read())
except Exception as e:
    print(e)

