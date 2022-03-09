# trabajando con ciclo while

contador = 0

while contador <= 10:
    print(contador)
    contador += 1

i = 5

while i >= 1:
    print(i)
    i -= 1

# trabajando con ciclo for

palabra = "Santiago"

for letra in palabra:
    print(letra)
    if letra == "i":
        print(f"Letra encontrada: {letra}")
        break
else:
    print("Fin del ciclo")

# numeros pares con for
for i in range(6):
    if i % 2 == 0:
        print(f"El valor es: {i}")

# numeros pares con for y continue
for i in range(10):
    if i % 2 != 0:
        continue
    print(f"El valor es: {i}")
    
    
# implementando enumerate en un ciclo for
print(f"\r\nimplementando enumerate en un ciclo for\r\n")
lista_numeros: list = [1,2,3,4,5,6,7,8,9,10]

print(f"{lista_numeros = }")
for key,value in enumerate(lista_numeros):
    print(f"Position: {key} - Value: {value}")
    
    
# implementado enumerate para obtener los numeros negativos de una lista
numeros: list = [3,67,-3,7,-87,0,-9]
for index,item in enumerate(numeros):
    if item < 0:
        print(f"El valor es: {item}")