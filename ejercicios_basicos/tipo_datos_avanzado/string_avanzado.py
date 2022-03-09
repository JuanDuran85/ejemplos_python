# trabajando con strings en python

# concatenacion automatica de string

varibale = 'Adios'
# mensaje = 'Nuevo' 'Mensaje' + varibale
# mensaje += 'Segundo mensaje' 'desde string'
# print(mensaje)

# para solicitar ayuda a la clase str
# help(str)

# para capitalizar la primera letra de un string
texto = "mensaje nuevo desde un string con capitalize"
print(texto.capitalize())

# concatenando cadenas iterables con el metodo join
lista = ['estudiando', 'con', 'universidad', 'python']
print(' '.join(lista))
lista = ('estudiando', 'con', 'universidad', 'python')
print(' '.join(lista))

# trabajando con string y join
cadena = "Aprendiendo Python 2021"
mensaje = '.'.join(cadena)
print(mensaje)

# trabajando con diccionarios y join
diccionario = {'nombre': 'Adrian', 'apellido': 'Gonzalez', 'edad': '21'}
llaves = ', '.join(diccionario.keys())
valores = ', '.join(diccionario.values())
print(llaves)
print(valores)

# trabajando con el metodo split
cadena = "Aprendiendo Python 2021"
mensaje = cadena.split()
print(mensaje)

cadena = "Java, Python, JavaScript, PHP, C, C++, C#"
mensaje = cadena.split(', ')
print(len(mensaje))
print(mensaje)

cadena = "Java, Python, JavaScript, PHP, C, C++, C#"
mensaje = cadena.split(', ', 2) # maxsplit es el numero de veces que se va a separar
print(len(mensaje))
print(mensaje)


# dar formato a un string
# %s es para string
# %d es para numeros enteros
# %f es para numeros flotantes
# %c es para caracteres
# %x es para numeros hexadecimales
# %o es para numeros octales
# %e es para numeros en notacion cientifica
# %g es para numeros flotantes con una notacion cientifica
# %r es para imprimir el valor de la variable
# los valores de las varibales se pasan dentro de una tupla
nombre = "Juan"
edad = 36
mensaje_con_formato = "Mi nombre es %s y mi edad es %d"%(nombre, edad)
print(mensaje_con_formato)

persona = ('Karla', 32, 5000.00)
mensaje_con_formato = "Mi nombre es %s y mi edad es %d y mi sueldo es %.2f"%persona
print(mensaje_con_formato)

persona = ('Maria', 22, 1500.00)
mensaje_con_formato = "Mi nombre es %s y mi edad es %d y mi sueldo es %.2f"
print(mensaje_con_formato%persona)

# trabajando directamente con format
nombre = "Juan"
edad = 28
sueldo = 3423.3454
mensaje_con_formato = "Mi nombre es {} y mi edad es {} y mi sueldo es {:.2f}".format(nombre, edad, sueldo)
print(mensaje_con_formato)

nombre = "Juan"
edad = 28
sueldo = 3423.3454
mensaje_con_formato = "Sueldo: {2:.2f}. Nombre: {0} y la edad de la persona: {1}".format(nombre, edad, sueldo)
print(mensaje_con_formato)
print("Sueldo: {s:.2f}. Nombre: {n} y la edad de la persona: {e}".format(n=nombre, e=edad, s=sueldo))

# usando diccionario con format
diccionario = {'nombre': 'Martes', 'apellido': 'Junio', 'sueldo': 2134.35445}
mensaje_con_formato = "Mi nombre es {nombre} y mi apellido es {apellido} y mi sueldo es {sueldo:.2f}".format(**diccionario)
print(mensaje_con_formato)
mensaje_con_formato2 = "Mi nombre es {dic[nombre]} y mi apellido es {dic[apellido]} y mi sueldo es {dic[sueldo]:.2f}".format(dic=diccionario)
print(mensaje_con_formato2)

# usando f-string o template literals
nombre = "Juan"
edad = 28
sueldo = 3423.3454
mensaje_con_formato = f"Mi nombre es {nombre} y mi edad es {edad} y mi sueldo es {sueldo:.2f}"
print(mensaje_con_formato)
print(nombre, edad, sueldo, sep=', ')

# multiplicar cadenas
cadena = 4*"Hola"
print(f'Resultado: {cadena}')

# multiplicacion de tuplas
cadena = 5*("Python","Programacion")
print(f'Resultado: {cadena}')

# multiplicacion de listas
lista = 10*[0]
print(f'Resultado: {lista}. Largo: {len(lista)}')

# caracteres de escape
resultado = 'Caracgter \' especial '
print(resultado)

# al utilizar el \b backspace se elimina el ultimo caracter
resultado = 'Se va a eliminar el ultimo punto.\b '
print(f"Resultado: {resultado}")
print("--------------------")

# escapando \
direccion = 'c:\\nuevo_directorio\\python'
print(f"Resultado: {direccion}")

# row string
resultado = r'Cadena sin procesar el salto de linea \n que lleva el cursor a la sigueinte linea'
print(resultado)
direccion = r'c:\nuevo_directorio\python'
print(f"Resultado: {direccion}")

# caracteres unicode
print('Hola\u0020Mundo')
print("Notacion simple para \\u0041 : \u0041")
print("Notacion extendida para \\U00000041: \U00000041")
print("Notacion simplificada en hexadecimal para \\x41: \x41")
print("Notacion simplificada para Smiling Face with Sunglasses Emoji: \U0001f60E")
print("Notacion simplificada para corazon: \u2665")

# caracteres ascii con chr

varibale = chr(65)
print(f"Resultado de chr(65): {varibale}")
variable = chr(38)
print(f"Resultado de chr(38): {variable}")

# caracteres del tipo byte
variable = b'\x41'
print(f"Resultado de b'\\x41': {variable}")
mensaje = b'Python'
print(f"Resultado de b'Python': {mensaje}")
print(mensaje[0])
print(chr(mensaje[0]))

# convertir string a bytes

string_var = "Programación con Python"
print(f"String original: {string_var}")
bytes_var = string_var.encode('utf-8')
print(f"Bytes convertido: {bytes_var}")

# convertir bytes a string
string_var_2 = bytes_var.decode('utf-8')
print(f"String convertido: {string_var_2}")

print(f"Son los mismos string: {string_var == string_var_2}")

# ocho formas de generar un bool False en python [1]

"""[1]
1. Comilla simple o doble ''/"" (cadena vacia)
2. Lista vacia []
3. Tupla vacia ()
4. Diccionario vacio {}
5. Entero 0
6. Flotante 0.0
7. None
8. bool del tipo False
"""
# ejemplo
variable = None

if variable:
    print("La variable es verdadera")
else:
    print("La variable es falsa")
    
# utilizando split y remove para trabajar con string

frease_string: str = "Ejemplo de frese en varibale del tipo string en python"
resultado_split: list = frease_string.split()
print(f"Resultado de split: {resultado_split}")
resultado_split.remove('en')
print(f"Resultado de remove: {resultado_split}")