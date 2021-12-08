# Dada una lista de palabras, vamos a quedarnos con la palabra con 
# más "a".

from functools import reduce

def total_a(w):
  """
  Devuelve el total de apariciones de la letra a
  Args:
    w: Palabra en formato string
  Returns:
    a: Número entero
  """
  a = 0
  for c in w.lower():
    if c == "a":
      a += 1
  return a

def more_a(w1, w2):
  """
  Devuelve la palabra con mayor número de a
  Args:
    w1: Palabra en formato string
    w2: Palabra en formato string
  Returns:
    Palabra en formato string
  """
  if total_a(w1) >= total_a(w2):
    return w1
  return w2

words = ["zapato", "amigo", "cosa", "amargada", "césped"]
print(reduce(lambda w1, w2: more_a(w1,w2), words))