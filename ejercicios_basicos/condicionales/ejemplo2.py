#comentario 1
"""
comentarios 2
"""
n1 = int(input("ingresa un numero entero: "))

if n1 % 2 == 0 :
  print("El número ingresado: ",n1," es par")
else :
  print("El número ingresado: ",n1," es impar")


if n1 > 0 :
  print("El número ingresado: ",n1," es positivo")
if n1 == 0 : 
  print("El número ingresado: ",n1," es cero")
if n1 < 0 :
  print("El número ingresado: ",n1," es negativo")

print("----------------")

dia = int(input("Ingresa el numero del dia correspondiente: "))

if dia == 1:
  print("Es lunes")
elif dia == 2:
  print("Es martes")
elif dia == 3:
  print("Es miercoles")
elif dia == 4:
  print("Es jueves")
elif dia == 5:
  print("Es viernes")
else:
  print("Otro dia...")