print("Hola mundo")
print('Hola mundo')
print(24+5)
print(24-5)
print(24*5)
print(24/5)
print(24%5)
print(24//5)
print(4**2)

nombre = input("Ingresa el nombre: ")
print("Bienvenido: ",nombre)

n1 = int(input("Ingresa un nùmero x: "))
n2 = int(input("Ingresa un nùmero y: "))
n3 = int(input("Ingresa un nùmero z: "))

print("El resultado de x+y es: ", n1+n2)
print("El resultado de (x*y)+(x*y) es: ", (n1*n2)+(n1*n2))
print("El resultado de (x*z)+(y*z) es: ", (n1*n3)+(n2*n3))
print("El resultado de (x*y)+z es: ", (n1*n2)+n3)

if n1 > 0 : 
  print("El numero ingresado: ", n1 ,"  es positivo")
else :
  print("El numero ingresado: ", n1 ,"  es negativo")