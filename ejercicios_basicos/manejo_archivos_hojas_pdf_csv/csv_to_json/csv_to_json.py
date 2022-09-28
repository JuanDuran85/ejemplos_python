import pandas as pd
import csv, json

try:
    data_from_csv: pd.DataFrame = pd.read_csv("ejercicios_basicos/manejo_archivos_hojas_pdf_csv/csv_to_json/archivocsv.csv")
    print(data_from_csv)
    print("Converted JSOn file below")
    data_transform: str = json.dumps(list(csv.reader(open("ejercicios_basicos/manejo_archivos_hojas_pdf_csv/csv_to_json/archivocsv.csv"))))
    print(data_transform)
except Exception as e:
    print("ERROR_READ_DATA")
    raise e