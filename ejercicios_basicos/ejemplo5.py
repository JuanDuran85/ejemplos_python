for n in range(1,10):
      print(n)

print("----------------")

for w in range(1,20,3):
  print(w)

print("----------------")

for w in range(20,1,-3):
  print(w)

print("----------------")

nombre = input("Ingresa tu nombre: ")
cantidad = int(input("Ingresa el numero: "))

for n in range(1,cantidad+1):
  print(nombre)

print("----------------")

n1 = int(input("Ingresa un numero entero: "))
i = 1
for x in range(1,11):
  print("",x,"*",n1,"=",x*n1)

print("----------------")

n1 = int(input("Ingresa un numero entero: "))

for x in range(1,n1):
  if (x % 7) == 0:
    print(x)