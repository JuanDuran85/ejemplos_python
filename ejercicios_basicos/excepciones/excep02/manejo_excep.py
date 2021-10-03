# trabajando con manejo de exceptiones
resultado = 0


try:
    numero_uno = int(input("Ingrese un numero: "))
    numero_dos = int(input("Ingrese otro numero: "))

    resultado = numero_uno + numero_dos
    resultado = numero_uno - numero_dos
    resultado = numero_uno * numero_dos
    resultado = numero_uno / numero_dos
    resultado = numero_uno % numero_dos

    print("La suma es: ", resultado)
    print("La resta es: ", resultado)
    print("La multiplicacion es: ", resultado)
    print("La division es: ", resultado)
    print("El modulo es: ", resultado)

except Exception as error:
    print("Error: No se pudo realizar la operacion: {}".format(error))
else:
    # unicamente se ejecuta cuando no existe alguna exception
    print("La operacion se realizo correctamente... else")
finally:
    # el bloque finally se ejecuta siempre, independientemente de si existe una exception o no
    print("La operacion se realizo correctamente... finally")