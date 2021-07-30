nombreFichero = "ejemplo1.txt";

fichero = open(nombreFichero,"w");
fichero.write("Este es un ejemplo de escritura\n");
fichero.write("Este es otro ejemplo de escritura\n");
fichero.write("\n");
for item in range(1,11):
    fichero.write("%d\n" % item);
fichero.close();

fichero = open(nombreFichero,"r");
result = fichero.readlines();
fichero.close();
print(result);

fichero = open(nombreFichero,"a");
valores = [1,2,3,4,5,6,7,8,9,10];
fichero.writelines(str(valores));
fichero.close();