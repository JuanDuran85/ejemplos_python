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