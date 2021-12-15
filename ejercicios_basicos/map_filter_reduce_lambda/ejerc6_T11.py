# Dada una lista de palabras, calcula el número de vocales de cada 
# una con map().

print('------------------------------------------------------------------')
print('Lista original (de paises):\n') 
paises_latam=['Bolivia','Chile', 'Colombia', 'Paraguay' ,'Peru', 'Venezuela']
print(paises_latam)
print('\nLista del número de vocal de cada pais ingresado:\n') 
def calc_num_vocals(paises_latam):
  """  
    Devuelve el número de vocales por palabra (pais) ingresada.
  Args:
    Lista de palabras (paises) en formato string.
  Salida:
    Lista con el número de vocales por palabra (pais).
  """ 
  cont_vocales=[]
  vocales=['a','e','i','o','u']
  for i in paises_latam:
    for j in i.lower():
      if j in vocales:
        cont_vocales.append(i)
  return len(cont_vocales)
print(list(map(calc_num_vocals, paises_latam))) 
print('------------------------------------------------------------------')