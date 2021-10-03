# trabajando con manejo de exceptiones

try:
    numero_uno = int(input("Ingrese un numero: "))
    numero_dos = int(input("Ingrese otro numero: "))

    print("La suma es: ", numero_uno + numero_dos)
    print("La resta es: ", numero_uno - numero_dos)
    print("La multiplicacion es: ", numero_uno * numero_dos)
    print("La division es: ", numero_uno / numero_dos)
    print("El modulo es: ", numero_uno % numero_dos)

except ValueError as error:
    print("Error: No se ingreso un numero: {}".format(error))
except ZeroDivisionError as error:
    print("Error: No se puede dividir entre cero: {}".format(error))
except Exception as error:
    print("Error: No se pudo realizar la operacion: {}".format(error))