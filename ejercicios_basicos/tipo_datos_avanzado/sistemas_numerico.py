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