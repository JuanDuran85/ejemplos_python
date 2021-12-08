#La función filter()
# Aplica una función a todos los elementos de un objeto iterable
# Devuelve un objeto generador, de ahí que usemos la función list() 
# para convertirlo a lista Como output, devuelve los elementos 
# para los cuales el aplicar la función ha devuelto True 

# Dada una lista numérica, vamos a filtrarla y quedarnos con los 
# números positivos. El resultado lo mostraremos en una lista.
print('-----------------------------------------------------------1')
nums = [-5, -3, 5, 2, 1, 3, -2, -9, 0.4, -0.01]
print(list(filter(lambda x: x > 0, nums)))

#  Con la ayuda de las funciones lambda, apliquemos filter() para
#  quedarnos con los números múltiplos de 7 de la siguiente lista
#  llamada
print('-----------------------------------------------------------2')
nums = [49, 57, 62, -147, 2101, 22]
print(list(filter(lambda x: (x % 7 == 0), nums)))

# La función proporcionada a filter() no tiene por qué ser lambda, 
# sino que puede ser una ya existente, o bien una creada por nosotros
# mismos. 
# Con las siguientes líneas de código vamos a obtener todas las
# palabras cuya tercera letra sea s haciendo uso de filter() y la
# función creada:

print('-----------------------------------------------------------3')
def third_letter_is_s(word):
  return word[1] == "a"
words = ["castaña", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
print(list(filter(third_letter_is_s, words)))
