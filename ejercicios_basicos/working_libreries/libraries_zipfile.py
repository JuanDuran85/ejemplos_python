"""_summary_

    Working with library zipfile
    
    You can unzip compressed files in python using the inbuilt zipfile library.

"""

import zipfile

try:
    with zipfile.ZipFile("/home/juan/Descargas/programacion/ejemplos_python/ejemplo_zip.zip","r") as data_file:
        data_file.extractall()
        print("Archivo extraido correctamente")
except Exception as e:
    print(f"Error in file: {e}")