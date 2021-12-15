# Dada una lista de palabras, quédate con filter() con las que tengan
# más vocales que consonantes. Necesitarás una función que devuelva
# si una palabra tiene más vocales que consonantes.

print('------------------------------------------------------------------')
paises_latam=['Bolivia','Chile', 'Colombia', 'Paraguay' ,'Peru', 'Venezuela']
print('La lista original es: ')
print(paises_latam)
print('------------------------------------------------------- ')
def cant_vocales(paises_latam):
    """
    Función para calcular la palabra con mayor vocales. 
        
    Args: Lista de Palabras (string).
    
    Salida: Lista de Palabras (string) con más vocales que consonantes.
    """
    vocales=['a','e','i','o','u']
    cont1, cont2=0,0
    for i in paises_latam:
        for j in i.lower():
            if j in vocales:
                cont1+=1
            else:
                cont2+=1
    if cont1>cont2:
     return cont1
print('La lista (subconjunto) con las palabras que contienen mas vocales:')
print(list(filter(cant_vocales, paises_latam)))
print('------------------------------------------------------------------')