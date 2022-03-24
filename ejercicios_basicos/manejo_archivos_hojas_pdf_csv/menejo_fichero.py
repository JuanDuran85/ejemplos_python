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


# --------------------------------------------------------------------------------------
# Reading Files using list comprehension. 
# First, we are opening a text ﬁle, and using a for loop, we are reading line by line. In the end, using strip we are removing all the unnecessary spaces.
path_file: str = '/home/juan/Descargas/programacion/ejemplos_python/ejercicios_basicos/manejo_archivos_hojas_pdf_csv/data.txt'

file_read: list = [line.strip() for line in open(path_file)]
print(file_read)

#Writing data to ﬁle
with open(path_file, 'a') as file:
    file.write("\nNuevos datos escritos en el archivo")

# other way to read data from file
with open(path_file) as file: 
    file_read = [line.strip() for line in file]
    print(file_read)
    
