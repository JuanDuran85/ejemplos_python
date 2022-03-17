"""_summary_

    Creando un fichero binario con la libreria pickle

"""

from io import BufferedWriter
import pickle

lista_colores: list = ["Verde", "Azul", "Rojo", "Amarillo"]

fichero_binario: BufferedWriter = open("fichero_binario.pckl", "wb")

pickle.dump(lista_colores, fichero_binario)

fichero_binario.close()