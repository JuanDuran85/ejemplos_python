# declarar variables
a, b = 'Uno', 'Dos'
print(a, b)

# swap o intercambio de variables
a, b = b, a
print(a, b)

# refresar multiples valores en una funcion


def min_max_valores(elementos):
    return min(elementos), max(elementos)


resultados = min_max_valores(list(range(1, 7)))
print(resultados)

# regresar la suma de una tupla

resultado_dos = sum((1, 2, 3, 4, 5))
print(resultado_dos)


def sumar(*args):
    return sum(args)


resultado_tres = sumar(*range(1, 6))
print(resultado_tres)
