# para imprimir todos los build-ins que tiene python
# print(dir(__builtins__))

# usando la funcion zip de python
lista_1 = (1,2,3,4)
letras = ['a','b','c','d','e','f','g','h','i','j','k']
identificador = 234,432,234,432
conjunto = {2,-5,7,3,88,4-2}
# del conjunto como es un set no se tiene orden, por lo tanto toma valores aleatorios
mezcla = zip(lista_1,letras, identificador, conjunto)
print(list(mezcla)) # una vez se leen y muestran los elementos de un zip, se terminan, por lo que se debe a volver a realizar el proceso
mezcla2 = zip(lista_1,letras, identificador)
print(tuple(mezcla2))

for valores in zip(lista_1,letras, identificador, conjunto):
    print(valores)
    
for v1, v2, v3, v4 in zip(lista_1,letras, identificador, conjunto):
    print(v1, v2, v3, v4)
    
# unzip y unpacking

mezcla_dos = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]
numeros, letras = zip(*mezcla_dos)
print(f"Numeros: {numeros}")
print(f"Letras: {letras}")

# ordenamiento con zip
lista_nueva = ['c', 'a', 'e', 't', 'b','d']
numeros = [5,6,1,0,3,2]
mezcla = zip(lista_nueva, numeros)
# sin ordenar
print(tuple(mezcla))
# ordenando
print(sorted(zip(lista_nueva, numeros)))

# crear un diccionario con zip y dos iterables
llaves = ["nombre", "apellido", "edad"]
valores = ["Juan", "Perez", "23"]
diccionario = dict(zip(llaves, valores))
print(diccionario)   

#actualizar un elemento de un diccionario
llave = ["edad"]
nueva_edad = [40]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)

# para mezclar dos listas en un solo elemento, pero perdiendo los valores que no tenga par
x: list = [1, 2, 3, 4, 5]
y: list = ['a', 'b', 'c']

print(f"{x = }")
print(f"{y = }")
result_x_y: list = list(zip(x, y))
print(f"{result_x_y = }")