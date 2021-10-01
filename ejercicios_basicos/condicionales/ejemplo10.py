# Operador ternario para uso del if en una linea
condition = True
print("Condicion verdadera...") if condition else print("Condicion falsa...")

# ----- ejercicio basico 10 -----

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 10:
    print("Estas entre 0 y 10 años de edad")
elif edad >= 10 and edad < 20:
    print("Estas entre 10 y 20 años de edad")
elif edad >= 20 and edad < 30:
    print("Estas entre 20 y 30 años de edad")
else:
    print("No se sabe...")

# otra menera de trabajar con los if-else

edad = int(input("Ingrese su edad: "))
mensaje = None

if 0 <= edad < 10:
    mensaje = "Estas entre 0 y 10 años de edad"
elif 10 <= edad < 20:
    mensaje = "Estas entre 10 y 20 años de edad"
elif 20 <= edad < 30:
    mensaje = "Estas entre 20 y 30 años de edad"
else:
    print("No se sabe...")

print(f"Tu edad es: {edad}. {mensaje}")

# ejercicio basico usando if-else

''' El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario proporcionará un valor entre 0 y 10.
Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F
cualquier otro valor debe imprimir: Valor desconocido '''

nota = int(input("Ingrese su nota: "))
mensaje = None

if 9 < nota <= 10:
    mensaje = "A"
elif 8 < nota <= 9:
    mensaje = "B"
elif 7 < nota <= 8:
    mensaje = "C"
elif 6 < nota <= 7:
    mensaje = "D"
elif 0 < nota <= 6:
    mensaje = "F"
else:
    mensaje = "Valor desconocido"

print(f"Su nota es: {nota}. Equivalente a: {mensaje}")