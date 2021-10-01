import emojis

def saludo ():
    print('-'*75)
    print(' Bienvenidos a este canal, diseñado y presentado por:elioduran60@gmail.com')
    print('-'*75)
saludo()
print('  °°°°°°°°°° SISTEMA DE CONVERSION DE TEMPERATURA °°°°°°°°°° ')
print('_'*75 )

def convertirtemp(unidad1, unidad2, valortemp): #Funcion de Conversion de Temperatura
    valortemp = float(valortemp)
    if unidad1=='C' and unidad2=='F':
        return valortemp*1.8 + 32 
    elif unidad1=='C' and unidad2=='K':
        return valortemp + 273.15
    elif unidad1=='F' and unidad2=='C':
        return (valortemp - 32)*0.5555556
    elif unidad1=='F' and unidad2=='K':
        return (valortemp - 32)*0.5555556 + 273.15 
    elif unidad1=='K' and unidad2=='C':
        return valortemp - 273.15
    elif unidad1=='K' and unidad2=='F':
        return (valortemp - 273.15)*1.8 + 32  

def caracteres(x):    #Funcion para rechazar simbolos
    a = ["/","*","+",",", "¿","|"]
    for i in a:
        for j in x:
            if(i==j):
                if i != " ":
                 rechazo=1
                return rechazo             
print('')
z= emojis.encode('¿Estas frio o caliente? :smile: ')
unidad1=input('Ingrese C ("Celsius"), o F ("Fahrenheit") o K ("Kelvin") para la temp. inicial: ')
unidad1=unidad1.upper()
if unidad1 =="C" or unidad1 =="F" or unidad1 =="K":
    print('_'*75)
    valortemp= input('Ingrese el valor de temperatura a convertir: ')
    print('_'*75)
    if not valortemp.isalpha() :
        x=list(valortemp)
        y=caracteres(x) 
        if y !=1:
            unidad2=input('Ingrese la letra "C", "F" o "K" para la temperatura a convertir: ')
            unidad2=unidad2.upper()
            if unidad2 =="C" or unidad2 =="F" or unidad2 =="K":
                print('_'*75) 
                convertirtemp(unidad1, unidad2, valortemp)
                total=convertirtemp(unidad1, unidad2, valortemp)
                print(f'>>> RESULTADO:  {valortemp} °{unidad1} = {total} °{unidad2}  ..* {z}')  
                print('-'*75) 
            else:    
                print ('>>> Error: la unidad de temperatura ingresada por Ud es invalida. \r\n')
        else:    
         print ('>>> Error: Usted ingresó un valor no válido.\r\n')
    else:    
        print ('>>> Error: Usted ingresó un valor no válido.\r\n')
else:    
    print ('>>> Error: la unidad de temperatura ingresada por Ud es invalida.\r\n')


