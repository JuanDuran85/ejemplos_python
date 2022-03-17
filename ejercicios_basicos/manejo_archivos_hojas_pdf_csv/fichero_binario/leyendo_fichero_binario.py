"""_summary_

    Leyendo un fichero binario con la libreria pickle

"""

from io import BufferedWriter
import pickle

fichero_binario = open("fichero_binario.pckl", "rb")

fichero_leido = pickle.load(fichero_binario)

print(fichero_leido)