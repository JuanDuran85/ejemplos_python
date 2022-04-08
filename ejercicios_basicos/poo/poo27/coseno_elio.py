# serie de potencias (serie de Maclaurin)
from math import factorial
def coseno(x,n):
    if n>=0:
        coseno=0
        if n %2 !=0:
            n +=1
            n=int(n/2) # Ésta condición es por el ejemplo que ellos dan allí, sino es asi, se elimina solo esta expresion
            for k in range(0,n+1):
                coseno+=((-1)**k)*((x)**(2*k))/(factorial(2*k))
        else:
            n=int(n/2) # Ésta condición es por el ejemplo que ellos dan allí, sino es asi, se elimina esa expresion
            for k in range(0,n+1):
                coseno+=((-1)**k)*((x)**(2*k))/(factorial(2*k))
        return (f'El valor aproximado del cos({x}) es: {coseno} ')
    return 'El valor ingresado de "n" no es un número válido.'    

print(coseno(float(input('Intoduzca (en radianes) el angulo "x"= ')),int(input('Intoduzca un número entero positivo "n"= '))))


