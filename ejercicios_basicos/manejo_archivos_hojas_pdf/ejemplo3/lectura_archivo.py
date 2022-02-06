# trabajando con archivos - lectura
try:
    archivo = open('archivos.txt', 'r', encoding='utf8')
    # para leer linea por linea
    for linea in archivo:
        print(linea)
except Exception as e:
    print(e)

try:
    archivo = open('archivos.txt', 'r', encoding='utf8')
    # para leer todas las lineas en el archivo
    print(archivo.readlines())
except Exception as e:
    print(e)

try:
    archivo = open('archivos.txt', 'r', encoding='utf8')
    # para leer una linea en especifico
    print(archivo.readlines()[2])
except Exception as e:
    print(e)

try:
    archivo = open('archivos.txt', 'r', encoding='utf8')
    # creando copia del archivo. 
    # "a" es para anexar información al archivo (no borra información)
    # "w" es para sobreescribir el archivo
    # "x" es para crear el archivo
    # "r" es para leer el archivo
    archivo_copia = open('archivos_copia.txt', 'a', encoding='utf8')
    archivo_copia.write(archivo.read())
    archivo_copia.close()
    archivo.close()
    print('Archivo copiado')
except Exception as e:
    print(e)