"""[summary]
    Dibujando una piramide o triangulo con *
"""

def triangulo(n):
    k=n-1
    for i in range(0,n):
        for _ in range(0,k):
            print(end=" ")
        k=k-1
        for _ in range(0,i+1):
            print("*",end=" ")
        print("\r")
n = int(input("Ingrese el numero de filas: "))
triangulo(n)