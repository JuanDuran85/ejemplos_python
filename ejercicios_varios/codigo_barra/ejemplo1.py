"""[summary]

La libreria barcode perte generar codigos de barra, en este caso se utilizara el numero de articulo europeo o EAN. Pero la libreria posee otros como CODE 128, CODE39, CODE 93, UPC, ISBN    

"""

from barcode import EAN13
from barcode.writer import ImageWriter

# se estable el directorio donde se guardara la informacion
directorio_guardar = r'/home/juan/Descargas/programacion/ejemplos_python/ejercicios_varios/codigo_barra'

# se establece el numero de codigo de barras. Importante: el modelo EAN debe tener 12 digitos.
numero_barra = "123456789012"

# luego se genera el codigo en el formato EAN13, pasando como argumento la instancia de la imagen
codigo_barra = EAN13(numero_barra, writer=ImageWriter())

# finalmente se guarda la imagen generada en el directorio especificado
codigo_barra.save(directorio_guardar + '/' + numero_barra)

