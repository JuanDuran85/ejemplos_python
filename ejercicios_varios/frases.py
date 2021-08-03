nombreFichero = "fases.txt";

print("Ingresa los datos solicitados");
f1 = input("Ingresa la primera frase: ");
f2 = input("Ingresa la segunda frase: ");
f3 = input("Ingresa la tercera frase: ");

fichero = open(nombreFichero, "w");
fichero.write("%s\n" % f1);
fichero.write("%s\n" % f2);
fichero.write("%s\n" % f3);
fichero.close();
print("Datos guardados correctamente");

fichero = open(nombreFichero, "a");
fichero.write("Nueva frase agregada");
fichero.close();

fichero = open(nombreFichero, "r");
result = fichero.readlines();
for x in result:
    print(x);
fichero.close();

# otra forma

nombreFichero = "fases2.txt";
lineas = [];

for x in range(0,3):
    frase = input("Ingresa la fresa numero %d: " % int(x+1));
    lineas.append(frase+"\n");

fichero_dos = open(nombreFichero, "w");
fichero_dos.writelines(lineas);
fichero_dos.close();

fichero_dos = open(nombreFichero, "a");
fichero_dos.write(input("Ingresa una nueva frase: ") + "\n");
fichero_dos.close();

fichero_dos = open(nombreFichero, "r");
result = fichero_dos.readlines();
fichero_dos.close();

for x in range(0, len(result)):
    print(str(x+1),":", result[x].rstrip());

print("Datos guardados correctamente");