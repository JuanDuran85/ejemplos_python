# alinear una cadena de texto

titulo = "Titulo de la pagina para centar"
print(titulo.center(50, "-"))
print(len(titulo.center(50, "-")))

titulo = "Nuevo titulo de la pagina para centrer"
print(titulo.center(len(titulo)+10, "-"))
# alinear una cadena de texto a la izquierda
print(titulo.ljust(len(titulo)+10, "-"))
# alinear una cadena de texto a la derecha
print(titulo.rjust(len(titulo)+10, "-"))
# reenplazar caracteres de una cadena por otro caracter
print(titulo.replace(" ", "-"))
# eliminar espacios en blanco o caracteres al inicio y al final de una cadena
ejemplo = "   --Esto es un ejemplo---    "
print(f"String original: {ejemplo}")
print(f"String modificado: {ejemplo.strip(' ')}")
print(f"String modificado: {ejemplo.strip(' ').strip('-')}")
# quitar caracteres de una cadena solo del lado izquierdo
print(f"String modificado: {ejemplo.strip(' ').lstrip('-')}")
# quitar caracteres de una cadena solo del lado derecho
print(f"String modificado: {ejemplo.strip(' ').rstrip('-')}")