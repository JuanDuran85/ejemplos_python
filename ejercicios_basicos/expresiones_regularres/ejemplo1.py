"""_summary_

    Expresiones regulares para cadenas de string con RE library
    
    $ para buscar un caracter al final de la cadena
    ^ para buscar un caracter al principio de la cadena
    

"""
import re
from typing import Match

cadena_texto: str = "Ejemplo de ER con Python"

resultado: Match[str] or None = re.search("de", cadena_texto)
resultado_dos: Match[str] or None = re.search("Python$", cadena_texto)
resultado_tres: Match[str] or None = re.search("^Ejemplo", cadena_texto)

if resultado:
    print(f"{resultado.group()} --> encontrado en la cadena: {cadena_texto}")
else:
    print(f"No se encontró la busqueda: {resultado }, en la cadena: {cadena_texto}")

if resultado_dos:
    print(f"{resultado_dos.group()} --> encontrado al final de la cadena: {cadena_texto}")
else:
    print(f"No se encontró la busqueda: {resultado_dos }, al final de la cadena {cadena_texto}")
    
if resultado_tres:
    print(f"{resultado_dos.group()} --> encontrado al inicio de la cadena: {cadena_texto}")
else:
    print(f"No se encontró la busqueda: {resultado_tres }, al inicio de la cadena: {cadena_texto}")
    

