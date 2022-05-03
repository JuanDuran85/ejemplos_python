# profundizando en los tipos de datos de python

# decimal
a = 10
print(a)

b = 0b1010
print(b)

c = 0o12
print(c)

d = 0xA
print(d)

# conversion de base numerica
# convertir un tipo de datos a otro
# convertir un entero en string con la funcion int
numero = int('23', 10)
print(f'numero: {numero}')

# convertir de binario en string a decimal con la funcion int
numero = int('10111', 2)
print(f'numero: {numero}')

# convertir de octal en string a decimal con la funcion int
numero = int('27', 8)
print(f'numero: {numero}')

# convertir de hexadecimal en string a decimal con la funcion int
numero = int('17', 16)
print(f'numero: {numero}')

# Convertir entero a decimal directamente en la cade con formato
error: int = 500
cadena_con_hexadecimal: str = 'Error en hexadecimal: %x' % error
cadena_con_hexadecimal_dos: str = 'Error en hexadecimal: {error:x}'.format(error=error)
cadena_con_hexadecimal_tres: str = f'Error en hexadecimal: {error:x}'
print(f"{cadena_con_hexadecimal = }")
print(f"{cadena_con_hexadecimal_dos = }")
print(f"{cadena_con_hexadecimal_tres = }")

# Si se quieren pasar varios valores, se debe utilizar una tupla
cadena: str = 'Nuevo mensaje %s: %x' % ('de error', error)
print(f"{cadena = }")