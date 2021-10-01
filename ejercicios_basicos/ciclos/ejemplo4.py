dividendo = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))

while divisor == 0:
  divisor = int(input("Ingresa el divisor: "))

print("la division de: ",dividendo, " entre: ", divisor, " es: ", dividendo / divisor)

print("---------------------------")

suma = 0
n = input("Ingresa un numero: ")
n = float(n)
while n != 0:
  suma = suma + n
  n = input("Ingresa un numero: ")
  n = float(n)

print("la suma es: ", suma)

print("---------------------------")

result = int(input("Ingresa el valor de la suma 32 + 44: "))
while result != 76:
  result = int(input("Ingresa el valor de la suma 32 + 44: "))
print("correcto, el resultado de sumar 32 + 44 es igual a: ", result)

print("---------------------------")

codigo = int(input("Ingresa el codigo de acceso: "))
clave = int(input("Ingresa la clave de acceso: "))

while not (codigo == 1234 and clave == 5000):
  print("Acceso denegado")
  codigo = int(input("Ingresa el codigo de acceso: "))
  clave = int(input("Ingresa la clave de acceso: "))

print("Bienvenido...")