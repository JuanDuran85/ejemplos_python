# Crea una lista de 20 tuplas de tamaño 2. La primera entrada será un número
# entero entre 1 y 20 y la segunda entrada contendrá una lista con los 10
# primeros múltiplos del número entero correspondiente. 
# 
# Por último, muestra las tablas de multiplicar del 1 al 20 con el formato “1 x 1 = 1”.

#[(1,[1,2,3,4,5,6,7,8,9,10]),(2,[2,4,6,8,10,12,14,16,18,20]),(3,[y]),(4,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(x,y),(20,y),]
print('------------------------------------------------------------------')

print(' --->PARTE 1: Crear lista de 20 tuplas de 2 elementos c/u.:\n ') 
lista1,lista2,lista3, lista4 =[], [], [], []
for i in range(1,21):    #Lista de 20 elementos.
    lista1.append(i)
    for j in range(1,11):
        lista2.append(j*i)
    lista1.append(lista2)  # Tuplas de 2 elementos
    lista2 = []
    lista3.append(tuple(lista1))
    lista1 = []
print('La Tupla de inical de 20 elemntos:\n  ')
print(lista1)
print('------------------------------------------------------------------\n') 
print(lista3)
print(len(lista3))

#PARTE 2: Muestra las tablas de multiplicar del 1 al 20 con el formato “1 x 1 = 1”
print('------------------------------------------------------------------\n') 
print(' --->PARTE 2: TABLAS DE MULTIPLICAR DEL 1 al 20:\n ') 
""" t=0
for i in range(1,21):
    t=t+1
    for j in range(1,21):
        tabla=i*j
        print(f' {j} *  {t} =  {tabla}' ) """
print('------------------------------------------------------------------')   