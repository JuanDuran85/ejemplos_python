"""_summary_

    Working with libraries: tarfile

"""

import tarfile
try:
    tar_file: tarfile.TarFile = tarfile.open("/home/juan/Descargas/programacion/ejemplos_python/ejemplo_tar_gz.tar.xz")
    tar_file.extractall()
    tar_file.close()
    print("Archivo extraido correctamente")
except Exception as e:
    print(f"Error in file: {e}")