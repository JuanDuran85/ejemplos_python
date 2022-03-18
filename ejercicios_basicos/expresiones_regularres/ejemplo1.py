"""_summary_

    Expresiones regulares para cadenas de string con RE library
    
    $ para buscar un caracter al final de la cadena
    ^ para buscar un caracter al principio de la cadena
    .* para buscar caracteres entre dos elementos en especifico
    \s para buscar espacios en blanco
    

"""
from re import search, findall, split
from typing import Match

# ------------------------------------ search ------------------------------------------------------

cadena_texto: str = "Ejemplo de Expresiones Regulares con Python"

resultado: Match[str] or None = search("de", cadena_texto)
resultado_dos: Match[str] or None = search("Python$", cadena_texto)
resultado_tres: Match[str] or None = search("^Ejemplo", cadena_texto)
resultado_cuatro: Match[str] or None = search("de.*con", cadena_texto)   

if resultado:
    print(f"{resultado.group()} --> encontrado en la cadena: {cadena_texto}")
else:
    print(f"No se encontró la busqueda: {resultado }, en la cadena: {cadena_texto}")

if resultado_dos:
    print(f"{resultado_dos.group()} --> encontrado al final de la cadena: {cadena_texto}")
else:
    print(f"No se encontró la busqueda: {resultado_dos }, al final de la cadena {cadena_texto}")
    
if resultado_tres:
    print(f"{resultado_tres.group()} --> encontrado al inicio de la cadena: {cadena_texto}")
else:
    print(f"No se encontró la busqueda: {resultado_tres }, al inicio de la cadena: {cadena_texto}")
    
if resultado_cuatro:
    print(f"{resultado_cuatro.group()} --> encontrado en la cadena: {cadena_texto}")
else:
    print(f"No se encontró la busqueda: {resultado_cuatro }, en la cadena: {cadena_texto}")
    
# ------------------------------------ findall ------------------------------------------------------

texto_cadena_dos: str = """
El vehiculo de Luis es blanco,
el vehiculo de Maria es negro,
el vehiculo de Juan es gris,
el vehiculo de Petra es blanco,
el vehiculo de Luisa es gris
"""

resultado_cinco: list = findall("vehiculo.*gris",texto_cadena_dos)

if resultado_cinco:
    print(f"Los elementos encontrados fueron: {resultado_cinco}")
else:
    print(f"No se encontraron elementos")
    
# ------------------------------------ split ------------------------------------------------------

texto_cadena_tres = "La silla es blanca y cuesta 90 mil"

resultado_seis: list = split("\s", texto_cadena_tres)
print(f"Los elementos encontrados fueron: {resultado_seis}")
