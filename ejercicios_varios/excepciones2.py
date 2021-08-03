try:
    nombre = input("Ingrese el nombre del archivo que desea buscar: ");
    archivo = open(nombre+".txt", "r");
    print("El archivo se encuentra abierto.");
except FileNotFoundError:
    print("El archivo no se encuentra.");
except IOError:
    print("Error de IO.");
else:
    resultado = archivo.readline();
    archivo.close();
    print("El contenido es: ");
    for x in range(0, len(resultado)):
        print(resultado[x].rstrip());
