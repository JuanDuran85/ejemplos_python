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

# obtener las primeras tres llaves del diccionario
print("\n obtener las primeras tres llaves del diccionario \n")
diccionario_usuarios = {
    'nombre': 'Maria',
    'edad': 23,
    'ciudad': 'Paris',
    'pais': 'Francia',
    'admin': True,
    'correo': 'maria@correo.com',
    'programas': ['Python', 'JavaScript', 'C++'],
}

print(f"{diccionario_usuarios = }")
for index,values in enumerate(diccionario_usuarios.items()):
    if index > 2:
        break
    print(values)
    
contador = 0
for values in diccionario_usuarios:
    print(values, diccionario_usuarios.get(values))
    contador += 1
    if contador > 2:
        break
    
# si se cuales son las llaves (nunca cambiaran)    
for contador_index in ['nombre','edad','ciudad']:
    print(contador_index,diccionario_usuarios[contador_index])
    