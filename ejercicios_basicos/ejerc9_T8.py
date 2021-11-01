# Dada una frase introducida por teclado, guarda en un conjunto todas
# las palabras que terminen por la letra indicada por el usuario.

print('------------------------------------------------------------------')
s = input("Introduce una frase o expresión: \n")
s=s.lower()
letra= input("Introduce una letra cualquiera: \n")
letra=letra.lower()
s=set(s.split())
set1=set()
for i in s:
    if i[-1]==letra:
        set1.add(i)
print(set1)
print('------------------------------------------------------------------')
