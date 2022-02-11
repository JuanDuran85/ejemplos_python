import pandas as pd

try:
    transfor_file = pd.read_csv('ejercicios_basicos/manejo_archivos_hojas_pdf/csv_to_xlsx/archivocsv.csv')
    transfor_file.to_excel('archivoxlsx.xlsx', sheet_name = 'CsvToXlsx', index = False)
    print(f"Transfor file to xlsx: {transfor_file}")
except Exception as e:
    print(f"Error --> {e}")