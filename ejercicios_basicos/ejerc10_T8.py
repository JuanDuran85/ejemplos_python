# Dada una frase introducida por teclado, guarda en un conjunto todas
# las palabras palíndromas

print('------------------------------------------------------------------')
s = input("Introduce una frase o expresión: \n")
s=s.lower()
s=set(s.split())
set1=set()
for i in s:
    if i == i[::-1]:
        set1.add(i)
print('El conjunto conformado por las palabras palíndromas es: \n')
print(set1)


print('------------------------------------------------------------------')






        
print('------------------------------------------------------------------')



