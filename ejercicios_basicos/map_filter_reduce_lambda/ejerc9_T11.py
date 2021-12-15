# Dada una lista de números reales, ordénalos con sorted() por valor
# absoluto de menor a mayor.

print('------------------------------------------------------------------')
l=[36.5,-10.11,3.1416,-41, -48.88,6.68,0.1]
print('Lista original de números reales):')
print(l) 
print('------------------------------------------------------------------')
l=list(map(lambda x : abs (x), l))
print('Lista transformada con su valor absoluto y ordenada de menor a mayor:')
print(sorted(l, key = lambda x: x))
print('------------------------------------------------------------------')