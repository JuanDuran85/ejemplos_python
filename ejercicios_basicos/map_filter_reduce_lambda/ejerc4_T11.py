# Dada una lista de números enteros, quédate con filter() con los que 
# tengan más de 5 divisores. Necesitarás una función que devuelva el
# número de divisores de un número dado.

print('------------------------------------------------------------------')
print('La lista original es:')
l=[36,10,191,41,48,668]
print(l)
print('------------------------------------------------------- ')
print('La lista resultante con los números con mas de 5 divisores es:')
def num_con5divrs(l):
    """
    Función para calcular el número de divisores de un número entero dado. 
        
    Args: Lista de Número enteros.
    
    Salida: Lista de Números con mas de 5 divisores.
    """
    l=[36,10,191,41,48,668]
    lr=[]
    for i in l: 
        cont=0
        for j in range(1,i+1):
            if i%j==0: 
                cont+=1
                if cont > 5:
                    lr.append(i)
                    break
    return list(filter(lambda cont: cont>5, lr))
print(num_con5divrs(l))
print('------------------------------------------------------------------')