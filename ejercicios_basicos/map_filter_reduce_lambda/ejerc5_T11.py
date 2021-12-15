# Dada una lista de palabras, quédate con reduce() con la palabra más
# larga. Necesitarás una función que compare dos palabras y devuelva
# la que tenga mayor longitud.

print('------------------------------------------------------------------')
from functools import reduce
paises_latam=['Bolivia','Chile', 'Colombia', 'Paraguay' ,'Peru', 'Venezuela']
def compara_palab(pais1, pais2):
  """  
    Funcion que devuelve la palabra con mayor número de caracteres
  Args:
    Lista de palabras (paises) en formato string.
  Salida:
    Una palabra (pais) en formato string de mayor caracteres.
  """  
  return pais1 if len(pais1) >= len(pais2) else pais2 
print(reduce(lambda pais1, pais2: compara_palab(pais1, pais2), paises_latam))
print('------------------------------------------------------------------')