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

  # cadenas de texto

  textoUno = "Resultados del produco {0}. y del producto {1}.";
  print(textoUno.format(n1,n2))

# realizar un programa que permita calcular el area de un triangulo mediante una funcion.

def area_triangulo(base,altura):
  return (base * altura)/2
  
print(f"El área del triangulo es: {area_triangulo(2,3)}")


frase1 = "Hola a todos desde 'Python'"
print(frase1)
frase2 = 'Hola a todos desde "Python"'
print(frase2)

nombre = input("Ingresa tu nombre: ")
print(nombre[2])
print(nombre[5])

print(len(nombre))
print(nombre.upper())
print(nombre.lower())
print(nombre[0:2])
print(nombre[-1])
print(nombre[::-1])