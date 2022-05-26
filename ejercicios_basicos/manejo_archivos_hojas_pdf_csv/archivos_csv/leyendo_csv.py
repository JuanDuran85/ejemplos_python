import csv

path_csv_local: str = "/home/juan/Descargas/programacion/ejemplos_python/ejercicios_basicos/manejo_archivos_hojas_pdf_csv/archivos_csv/archivocsv.csv"

with open(path_csv_local) as file_csv:
    reader_csv: csv.DictReader = csv.DictReader(file_csv, delimiter=';')
    for line in reader_csv:
        print(line)
        
        
#                Dialectos

# Los dialectos ayudan a agrupar patrones de formato específicos
#  como el delimitador, las comillas, los espacios adicionales 
# tras los delimitadores...

# En vez de indicar todos esos parámetros al método .reader(),
# vamos a crear nuestro dialecto, my_dialect, con el método
# .register_dialect() y se lo vamos a pasar al parámetro dialect
# de .reader()

print('Sin Dialecto (metodo convencional .reader())')

with open(path_csv_local, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print('\nMetodo Dialect ***************************')
csv.register_dialect("my_dialect",
                     delimiter = ";",
                     skipinitialspace = True,
                     quoting = csv.QUOTE_NONE)

with open(path_csv_local, "r") as f:
    reader = csv.reader(f, dialect='my_dialect')
    for row in reader:
        print(row)