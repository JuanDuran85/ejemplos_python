# utilizando with para manejar archivos en python (content manager)

with open('archivos_copia.txt', 'r', encoding="utf8") as archivo:
    for linea in archivo:
        print(linea, end='')