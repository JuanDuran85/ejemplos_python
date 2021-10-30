
opciones = {
    1: 'Crear usuario',
    2: 'Mostrar usuario',
    3: 'Actualizar usuario',
    4: 'Eliminar usuarios',
    5: 'Salir'
}

opcion = None

while opcion != 5:
    try:
        print("\n ")
        print("Menú de selección: ".center(50, "-"))
        print("1. Crear Usuario")
        print("2. Mostrar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        print("")

        opcion = int(input("Ingrese una opción: "))
        opciones[opcion]()

    except Exception as e:
        print(e)
        print("Ingrese una opción válida")
        opcion = None