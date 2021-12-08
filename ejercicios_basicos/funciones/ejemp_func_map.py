#                   La función map()
# 1.- Aplica una misma función a todos los elementos de un objeto iterable
# 2.- Devuelve un objeto generador, de ahí que usemos la función list() 
#     para convertirlo a lista 
# 3.- Como output, devuelve el resultado de aplicar la función a cada elemento

#Con la ayuda de las funciones lambda, apliquemos map() para calcular las
# longitudes de las siguientes palabras:

print('-----------------------------------------------------------1')

words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
print(list(map(lambda w: len(w), words)))

# OJO: Sin embargo, para este caso en concreto no haría falta usar 
# funciones lambda, pues podríamos hacer directamente:
print('-----------------------------------------------------------2')
print(list(map(len, words)))

# Dada una lista numérica, vamos a filtrarla y quedarnos con los
# números positivos. El resultado lo mostraremos en una lista.