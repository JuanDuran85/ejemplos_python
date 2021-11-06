import urllib
from urllib.request import urlopen

# leer contenido online
# utilizamos with para abrir y cerrar de manera automatica el archivo


req = urllib.request.Request('http://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt', headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})

palabras = []

with urlopen(req) as contenidos:
    data = contenidos.read().decode('utf-8')
# convertir todo a mayusculas
print(data.upper())
# convertir todo a minusculas
print(data.lower())
# Inicia con
print(data.startswith('En GlobalMentoring.com.mx'))
# finaliza con
print(data.endswith('GlobalMentoring.com.mx'))

with open('GlobalMentoring.txt', 'w', encoding='utf8') as archivo:
    archivo.write(data)
    print("Archivo creado")

with open('GlobalMentoring.txt', 'r', encoding='utf8') as archivo:
    for linea in archivo:
        palabras_encontradas = linea.split()
        for palabra in palabras_encontradas:
            palabras.append(palabra)

print(palabras)

# contando cantidad de palabras
print(f"La cantidad de palabra 'Universidad' es: {palabras.count('Universidad')}")

# islower e isupper
string_mensaje = """
FUNDADOR DE GLOBALMENTORING.COM.MX
"""
print(string_mensaje.islower())
print(string_mensaje.isupper())

