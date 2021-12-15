# Dada una lista de números enteros, calcula el número anterior con 
# map()
print('------------------------------------------------------------------')
l=[36,10,191,41,48,668]
print('Lista original de números enteros):')
print(l) 
print('------------------------------------------------------------------')
num_anterior=list(map(lambda x : (x-1), l))
print('Lista transformada con números enteros cada uno anterior a la lista original:')
print(num_anterior)
print('------------------------------------------------------------------')