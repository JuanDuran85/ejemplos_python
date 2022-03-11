"""_summary_

    Working with libraries and variables "varname"

"""

from varname import nameof

# using nameof to get the variable name
nombre_variable: str = 'Varibale con nombre en string'
numero_variable: int = 354

print(f"{nameof(nombre_variable)}: {nombre_variable}")
print(f"{nameof(numero_variable)}: {numero_variable}")