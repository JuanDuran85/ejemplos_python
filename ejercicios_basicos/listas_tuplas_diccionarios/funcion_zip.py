# para imprimir todos los build-ins que tiene python
# print(dir(__builtins__))

# usando la funcion zip de python
lista_1 = (1,2,3,4)
letras = ['a','b','c','d','e','f','g','h','i','j','k']
mezcla = zip(lista_1,letras)
print(list(mezcla)) # una vez se leen y muestran los elementos de un zip, se terminan, por lo que se debe a volver a realizar el proceso
mezcla2 = zip(lista_1,letras)
print(tuple(mezcla2))