# Crea una función que dado un color en hexadecimal devuelva una lista
# de 3 posiciones, cada una de ellas correspondiente al valor R, G o B
# en este orden. Los valores de RGB varían entre 0 y 255.

print('------------------------------------------------------------------')
def conv_hexadec(num_hexadec):
    """
    Función que convierte valores de un color en hexadecimal a (R,G,B).

    Args: Valor o Código hexadecimal en hexadecimal (correspondiente a un color) .

    Salida: lista de 3 posiciones con el Código decimal:(RR,GG,BB).
    """
    #num_hexadec=print
    num_hexadec=num_hexadec.upper()
    num_hexadec=list(num_hexadec)
    r, g, b =[], [], [] 
    n =-1
    if len(num_hexadec)==6:
        for i in num_hexadec:
            n +=1
            if not i.isnumeric(): #Cuando el digito es alfabetico de A....F:
                v1, v2=0,0
                if   i=='A': 
                    v1=10*16
                    v2=10 
                elif i=='B':
                    v1=11*16
                    v2=11     
                elif i=='C': 
                    v1=12*16
                    v2=12 
                elif i=='D':
                    v1=13*16
                    v2=13 
                elif i=='E':
                    v1=14*16
                    v2=14
                elif i=='F':
                    v1=15*16
                    v2=15
                if   n==0: r1=v1  # 1er. dígito 
                elif n==1: r2=v2  # 2do. dígito
                elif n==2: g1=v1  # 1er. dígito
                elif n==3: g2=v2  # 2do. dígito
                elif n==4: b1=v1  # 1er. dígito
                elif n==5: b2=v2  # 2do. dígito
                
            else: # Cuando el digito es un número del 0 al 9:
                if   n==0: r1=(int(i))*16 # 1er. dígito
                elif n==1: r2=(int(i))    # 2do. dígito
                if   n==2: g1=(int(i))*16 # 1er. dígito
                elif n==3: g2=(int(i))    # 2do. dígito
                if   n==4: b1=(int(i))*16 # 1er. dígito
                elif n==5: b2=(int(i))    # 2do. dígito
        return print(f'El Código decimal es: ({r1+r2},{g1+g2},{b1+b2})')
    else:
        print('** Atención: El valor introducido no es válido')
conv_hexadec((input('Introduzca el numero color en número hexadecimal:')))
print('------------------------------------------------------------------')