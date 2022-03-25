"""_sumary_

    Using pprint library

"""

import pprint

tabla_datos = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "direccion": 'abc',
    "telefono": '123'
}
print(tabla_datos)
for_print = pprint.PrettyPrinter(indent=4, width=41, compact=True)
for_print = pprint.pformat(tabla_datos)
print(for_print)

#-------------------------------------------------------------------------