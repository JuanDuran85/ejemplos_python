# Dada una lista de palabras, quédate con reduce() y map() con la palabra
# con más consonantes. Necesitarás una función que cuente el número de
# consonantes de una palabra y otra que dados dos números, devuelva el 
# mayor.

print('------------------------------------------------------------------')
from functools import reduce
print('Lista original (de paises):') 
paises_latam=['Bolivia','Chile', 'Colombia', 'Paraguay' ,'Peru', 'Venezuela']
print(paises_latam)
def calc_num_vocals(paises_latam):
  """  
    Devuelve el número mayor de consonantes de las palabra (pais) ingresadas.
  Args:
    Lista de palabras (paises) en formato string.
  Salida:
    Valor del número de consonantes contenido en la palabra (pais) que mas tiene esos caracteres.
  """ 
  consonantes=[]
  vocales=['a','e','i','o','u']
  for i in paises_latam:
    for j in i.lower():
      if not j in vocales:
        consonantes.append(i)
  return len(consonantes)
calc_num_vocals(paises_latam)
aux=list(map(calc_num_vocals, paises_latam))
print(f'\nLista con el número de consonantes de los diferentes paises: {aux} ')
def bigger_than(a, b):
    if a > b:
        return a
    return b
print(f'-->Valor o cantidad de la palabra con mas consonantes: {reduce(bigger_than,(aux))} \n')
print('------------------------------------------------------------------')