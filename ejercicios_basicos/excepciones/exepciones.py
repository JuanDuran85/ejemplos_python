try:
    fichero = open("ejemplo.txt","r");
    lineas = fichero.readlines();
    fichero.close();
    print(lineas);
except Exception:
    print("Error al abrir el fichero");

print("Fin del programa")

# otra forma implementando else

try:
    fichero = open("ejemplo.txt","r");
except Exception:
    print("Error al abrir el fichero");
else:
    lineas = fichero.readlines();
    fichero.close();
    print(lineas);

print("Fin del programa")