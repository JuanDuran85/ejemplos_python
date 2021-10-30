# trabajando con valores booleanos o tipo bool
# tipos numericos. 
# Falso para valores de cero, cadena vacia, lista vacia, diccionario vacio,
valor = 0.0
resultado = bool(valor)
print(f"Bool para el valor: {valor} es {resultado}")
valor = 1234.0
resultado = bool(valor)
print(f"Bool para el valor: {valor} es {resultado}")
valor = ""
resultado = bool(valor)
print(f"Bool para el valor(cadena vacia): {valor} es {resultado}")
valor = []
resultado = bool(valor)
print(f"Bool para el valor: {valor} es {resultado}")
valor = ()
resultado = bool(valor)
print(f"Bool para el valor: {valor} es {resultado}")
valor = {}
resultado = bool(valor)
print(f"Bool para el valor: {valor} es {resultado}")
valor = None
resultado = bool(valor)
print(f"Bool para el valor: {valor} es {resultado}")
valor = True
resultado = bool(valor)
print(f"Bool para el valor: {valor} es {resultado}")

