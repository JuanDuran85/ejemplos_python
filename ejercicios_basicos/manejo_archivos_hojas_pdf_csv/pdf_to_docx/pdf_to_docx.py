"""
Using pdf2docx library
"""

from pdf2docx import Converter

#-----------------------------------------------------------------------------
# We can use either the Converter class, or a wrapped method parse() to convert all/specified pdf pages to docx. Multi-processing is supported in case pdf file with a large number of pages.
#-----------------------------------------------------------------------------
pdf_file: str = "/home/juan/Descargas/programacion/ejemplos_python/Numpy Handbook.pdf"
docx_file = 'nh_convert.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
print("Archivo convertido")
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------