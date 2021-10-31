                #           El método de unpacking
 #  Podemos extraer los valores de una tupla en variables. Este 
 # proceso es conocido como unpacking
 # Ejemplo: 

fruits = "Cereza", "Kiwi", "Pera", "Naranja"
# Nota: Con paréntesis (o si usar parentisis. Para las tuplas da igual)

(fruit1, fruit2, fruit3, fruit4) = fruits # Una variabke...un valor, 
                                         #caso contrario daría Error!

print('------------------------------------------------- Caso Gral. s/* ')
print(fruit1)
print(fruit2)
print(fruit3)
print(fruit4)

# *** ¡Cuidado! El número de variables debe coincidir con el número 
# de elementos de la tupla, sino dará error.
# Pero se puede usar un asterisco # para guardar los elementos
# restantes en una lista:

fruits = "Cereza", "Kiwi", "Pera", "Naranja", "Melocotón", "Sandía", "Melón"

fruit1, fruit2, *restFruits = fruits
print('------------------------------------------------------- c/* - 1 ')
print(fruit1)
print(fruit2)
print(restFruits)


fruit1, *restFruits, fruit2 = fruits
print('------------------------------------------------------- c/* - 2 ')
print(fruit1)
print(restFruits)
print(fruit2)

*restFruits, fruit1, fruit2 = fruits
print('------------------------------------------------------- c/* - 3 ')
print(restFruits)
print(fruit1)
print(fruit2)


print('------------------------------------------------------- Piso_abajo ')
(fruit1, *_, fruit2, fruit3) = fruits

print(fruit1)
print(fruit2)
print(fruit3)


# ----------------------------------------------------------------------
""" otros ejemplos y usos de las tuplas y listas con el Unpaking"""
# ----------------------------------------------------------------------

# el * se utiliza para desempaquetar tuplas y crea una lista
numeros = (1,2,3,4,5,6,7,8,9,10);
print("Desempaquetado de tuplas 1");
uno, dos, *resto = numeros;
print("uno: ", uno);
print("dos: ", dos);
print("resto: ", resto);

# el *_ se utiliza para ignorar los elementos restantes de la tupla
numeros = (1,2,3,4,5,6,7,8,9,10);
print("Desempaquetado de tuplas 2");
uno, dos, *_ = numeros;
print("uno: ", uno);
print("dos: ", dos);

# el *_ se utiliza para ignorar los elementos restantes de la tupla
numeros = (1,2,3,4,5,6,7,8,9,10);
print("Desempaquetado de tuplas 3");
uno, dos, *_, nueve, diez = numeros;
print("uno: ", uno);
print("dos: ", dos);
print("nueve: ", nueve);
print("diez: ", diez);

# el *_ se utiliza para ignorar los elementos restantes de la tupla y el _ para omitir un valor en especifico
numeros = (1,2,3,4,5,6,7,8,9,10);
print("Desempaquetado de tuplas 4");
uno, _, tres, *resto, nueve, diez = numeros;
print("uno: ", uno);
print("tres: ", tres);
print("resto: ", resto);
print("nueve: ", nueve);
print("diez: ", diez);
