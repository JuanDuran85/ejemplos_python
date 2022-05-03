"""_summary_

  Funciones
  
"""

print()
print("-----------------------")
print("Funciones")
print("-----------------------")
print()

def subrayar(espacio):
  for _ in range(0,espacio):
    print("-",end="")
  print()

print("Mensaje 1")
subrayar(23)
print("Mensaje 2")
subrayar(12)
print("Mensaje 3")
subrayar(19)

print()
print("-----------------------")
print("Funciones 2")
print("-----------------------")
print()

def comparacion (n1,n2):
  if(n1 > n2):
    return "El numero " + str(n1) + ", es mayor"
  elif (n1 < n2):
    return "El numero: " + str(n2) + ", es mayor"
  else:
    return "Los numeros son iguales"

result = comparacion(7,6)
print(result)

print()
print("-----------------------")
print("Funciones 3")
print("-----------------------")
print()

def sumas(n1,n2,n3):
  return n1+n2+n3

n1 = int(input("Ingresa el primero numero: "))
n2 = int(input("Ingresa el segundo numero: "))
n3 = int(input("Ingresa el tercer numero: "))
print("El resultado de sumar: 4,5,3 es: ", sumas(n1,n2,n3))

print()
print("-----------------------")
print("Funciones 4")
print("-----------------------")
print()

def textos(cadena,letra):
  i = 0
  for x in cadena:
    if (x == letra):
      i += 1
  return i

cadena = input("Ingresa una palabra: ")
letra = input("Ingresa una letra: ")
print("La letra: "+letra+" , se encuentra repetida: "+str(textos(cadena,letra))+" veces")

print()
print("-----------------------")
print("Funciones 5")
print("-----------------------")
print()

def linea(letra1, letra2, repeticion):
  for _ in range(repeticion):
    print(letra1, end="")
    print(letra2, end="")

letra1 = input("Ingresa una letra o simbolo cualquiera: ")
letra2 = input("Ingresa una letra o simbolo cualquiera: ")
repeti = int(input("Ingresa un numero entero para repetir: "))
linea(letra1, letra2, repeti)

