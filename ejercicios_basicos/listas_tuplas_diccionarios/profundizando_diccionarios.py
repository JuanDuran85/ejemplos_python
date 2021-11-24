from pprint import pprint as pp
# profundizando en diccionarios
# Los diccionarios guardan un orden a diferencia de los set
# los diccionarios son mutables, pero las llaves deben ser inmutables
# los diccionarios no tienen llaves duplicadas, por lo tanto, si existe la llave la modifica o actualiza, si no existe la crea.
# si no se encuentra una llave, se genera o lanza una exception de key error

diccionario = {'nombre': 'Juan', 'apellido': 'Perez', 'edad': 23}

# metodo get recupera una llave, si no existe no lanza una exception. Se puede regresar un valor en el caso que no exista la llave
print(diccionario.get('Nombre', 'No se enconetró la referencia'))

# el metodo ser modifica el diccionario, si no se encuentra la llava agrega el valor por defecto
nombre = diccionario.setdefault('Nombre', 'No se encontró la llave')
print(diccionario)

# imprimir con pprint
pp(diccionario, sort_dicts=True)