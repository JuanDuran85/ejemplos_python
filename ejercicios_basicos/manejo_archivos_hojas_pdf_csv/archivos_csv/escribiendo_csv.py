"""_summary_

    Working with csv files

"""

import csv

def csv_writer(data: list, path: str) -> None:
    """
        Write data to a CSV file
    """
    try:
        with open(path, "w", newline='') as csv_file:
            writer_data = csv.writer(csv_file, delimiter=",")
            for line in data:
                writer_data.writerow(line)
        print("Se ha escrito el archivo correctamente")
    except Exception as e:
        print(f"Error: {e}")
            
if __name__ == '__main__':
    data: list = [
        "first_name,last_name,city".split(','),
        "Jhon,Smith,London".split(','),
        "Jhon,Doe,Paris".split(','),
        "Maria,Perez,Madrid".split(','),
    ]
    path_file = '/home/juan/Descargas/programacion/ejemplos_python/ejercicios_basicos/manejo_archivos_hojas_pdf_csv/archivos_csv/archivocsv.csv'
    
    csv_writer(data,path_file)