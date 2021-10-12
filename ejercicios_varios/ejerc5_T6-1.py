# Crea un programa que lea números enteros hasta que introduzca el 0 y 
# devuelva un diccionario con la cantidad números pares e impares 
# introducidos

print('------------------------------------------------------------------')    
n=0
n= int(input('Introduzca un número entero cualquiera, ó el "0 (cero) para SALIR:  \n '))

par=[]
impar=[]
key=[]
cont=0
print('------------------------------------------------------------------')
while n!=0:
    cont +=1
    key.append(cont)
    if n%2==0:
     par.append(n) 
    else:
     impar.append(n)     
    n= int(input('Introduzca un número entero cualquiera, ó el "0 (cero) para SALIR:  \n '))
    if n==0:
        print('Ud. salió del programa') 
        break
par.sort()
impar.sort()
print('------------------------------------------------------------------')    
print(f'La lista ordenada de números  PARES  es: {par} ')
print(f'La lista ordenada de números IMPARES es: {impar} ')
print('------------------------------------------------------------------')  
print('------------------------------------------------------------------')  
dic1={} 
print('El Diccionario resultante de números PARES  es: ')
for i in range(len(par)):
    dic1[key[i]]=par[i]
print(dic1)
print('------------------------------------------------------------------') 
dic2={} 
print('El Diccionario resultante de números IMPARES es: ')
for i in range(len(impar)):
    dic2[key[i]]=impar[i]
print(dic2)
print('------------------------------------------------------------------') 
print('El Diccionario final resultante es: ')
dic_resultante={}
dic_resultante["#Pares"]=par
dic_resultante["#Impares"]=impar
print(dic_resultante)
print('------------------------------------------------------------------') 