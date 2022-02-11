import csv

with open("/home/juan/Descargas/programacion/ejemplos_python/ejercicios_basicos/manejo_archivos_hojas_pdf_csv/lectura_csv/archivocsv.csv") as file_csv:
    reader_csv = csv.DictReader(file_csv, delimiter=';')
    for line in reader_csv:
        print(line)