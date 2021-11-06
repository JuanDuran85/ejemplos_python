# unpacking de una tupla

# en este caso se convierten los valores en una tupla
valores = 1,2,3,4,5
print(valores)
print(type(valores))

# agregando varias variables
valor1, valor2, valor3 = 1,2,3
print(valor1, valor2, valor3)

# omitiendo valores con _
valor1, valor2, _ , valor4, valor5 = 1,2,3,4,5
print(valor1, valor2, valor4, valor5)

# asignando varios valores a una sola varibale mediante el * como una lista
valor1, valor2, *valor3 = 1,2,3,4,5,6,7,8,9,10,11,12,13
print(valor1, valor2, valor3)

# asignando varios valores a una sola varibale mediante el * como una lista y asignando algunos valores a una variable al inicio y al final
valor1, valor2, *valor3, valor5, valor6 = 1,2,3,4,5,6,7,8,9,10,11,12,13
print(valor1, valor2, valor3, valor5, valor6)

# trabajando con el operador *_, el cual, si guarda los valores restantes, solo que no se utiliza.

def retornar_valores():
    return [1,2,3],{"nombre": "Juan"},3,4,5

valor1, valor2, *_ = retornar_valores()
print(valor1, valor2)

# ejemplo usuando unpacking usando el metodo partition
hora = "12:30"
hora_separada = hora.partition(":")
print(hora_separada)
hora, _ , minutos = hora_separada
print(hora, minutos)
