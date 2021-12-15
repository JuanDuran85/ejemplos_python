# Dada una lista de palabras, ordénalos con sorted() por número de 
# consonates de mayor a menor.
print('------------------------------------------------------------------')
paises_latam=['Bolivia','Chile', 'Colombia', 'Paraguay' ,'Peru', 'Venezuela']
print('Lista original (de paises):')
print(paises_latam) 
print('------------------------------------------------------------------')
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
print('Lista ordenada de mayor a menor por número de consonantes de cada entrada (pais)')
print(sorted(list(map(calc_num_vocals, paises_latam)), reverse = True))
print('------------------------------------------------------------------')