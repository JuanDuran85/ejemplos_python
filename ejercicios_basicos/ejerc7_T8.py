""" 
Dada una frase introducida por teclado, 
guarda en un conjunto la primera letra 
de cada palabra sin hacer uso del método 
.split().
"""

print('------------------------------------------------------------------')
s= input("Introduce una frase o expresión: \n")
s=s.lower()
s=list(s)
set1=set(s[0])
set2=set()
j=1
''' Quitar el primero for, no hace falta. Ese for lo que hace es que recorrar toda la cadenada para cada letra e intenta agregar una y otra vez la misma letra. no la agrega porque usas el set. Por lo tanto, no hace falta '''
for j in range(len(s)):
        if s[j]==" ":
            set2.add(s[j+1])
print(f'El conjunto resultante es:-->',set1|set2)
print('------------------------------------------------------------------')

