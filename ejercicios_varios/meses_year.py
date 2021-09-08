# meses del año
mes = int(input("Introduce un mes (1-12): "))

if mes == 1:
    print("El mes es Enero")
elif mes == 2:
    print("El mes es Febrero")
elif mes == 3:
    print("El mes es Marzo")
elif mes == 4:
    print("El mes es Abril")
elif mes == 5:
    print("El mes es Mayo")
elif mes == 6:
    print("El mes es Junio")
elif mes == 7:
    print("El mes es Julio")
elif mes == 8:
    print("El mes es Agosto")
elif mes == 9:
    print("El mes es Septiembre")
elif mes == 10:
    print("El mes es Octubre")
elif mes == 11:
    print("El mes es Noviembre")
elif mes == 12:
    print("El mes es Diciembre")
else:
    print("Mes no válido")


# el mismo ejercicio pero con diccionarios
print("Ejercicio usando diccionario")

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

meses_tupla = (
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
)

mes = int(input("Introduce un mes (1-12): "))

try:
    if meses_tupla[mes]: 
        print(f"El mes es {meses[mes]}")
except IndexError as error:
    print("Error en el mes")
    print(error)