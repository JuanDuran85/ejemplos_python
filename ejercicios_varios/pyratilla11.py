from functools import reduce
from numpy import random
print('------------------------------------------------------------------')
print(' ***** ¡CONTINUA LA AVENTURA PARA RECORRER LAS ISLAS! ****')
print('---------------/El viaje a Isla Torva/------------------\n')

 # Parte I-A: Crea un diccionario con los objetivos y los golpes que hay 
 # que dar a Valrock 
hit={ "brazaleteD": 8, "brazaleteI": 8, "cinturon": 14 }
l1,l2=[],[]
for key, valor in hit.items():
        l1.append(key)
        l2 .append(valor)
total_hits=reduce(lambda x, y: x+y, l2)
print('-------------Tripulación ataquemos al monstruo...!!!!-------------')
print('Total de golpes que habrá de darle al Valrock es: ', total_hits )
print('------------------------------------------------------------------')
 # Parte I-B: Crea un método llamado attack que por parámetro reciba el 
# objetivo, target, en formato string y muestre por pantalla la frase:
# "Pyratilla ha atacado al target".
l1=sorted(l1)
def attack(l1):
  """
  Args:
   
  Salida:
  """ 
      
  target=l1
  return '¡Pyratilla ha atacado con el:'
hit= {"brazaleteD": 8, "brazaleteI": 8, "cinturon": 14}   
msj="¡Oh, no! ¡Pyratilla ha fallado!" 
x=0
for key in hit:
    n,m,dispF,dispV =0,0,0,0
    print(f'** El objetivo a destruir es el: {key} ')
    if key=="brazaleteD" or key=="brazaleteI" or key=="cinturon":
        while m < (hit[key]):
          ataq=random.randint(0,2)
          if (dispF+ dispV)==5:                  
             print("¡Un segundo! ¡Hay que recargar los 5 cañones!")
             dispF, dispV=0,0     
          if ataq ==0:
            print(msj)
            dispF +=1
          else:
            m +=1
            print(attack(l1), key)
            dispV +=1
            if m==hit[key]:
              x +=1
              print(f'ATENCION:¡El {key} ha sido eliminado!\n')
              if x==3:
                print('"¡¡¡El Valrock ha sido eliminado!!!" \n')
print('-----------¡Juega con Pyratilla a palabras encadenadas------------')

# Parte II-a: Crear la función palabras_encadenadas() que te permita hacer
# una partida de este juego crea una función helper llamada valid_option()
# que compare la última letra de la palabra anterior con la primera de la
# nueva. Si # coinciden, devuelve True. De lo contrario, devuelve False. 

from functools import reduce
def valid_option(w1, w2):
    if w1[-1] == w2[0]:
        return True
    else:
        return False
w1 = input("Introduce la 1ra. palabra: ")
w2 = input("Introduce la 2da. palabra: ")
  
def palabras_encadenadas(w1, w2):
    played_words = []
    if w1==w2:
        print('No puedes introducir la misma palabra \n')
    else: 
        if valid_option(w1, w2):
            print('"Felcitaciones Ud ha ganado..!! \n')
            played_words.append(w1)
            played_words.append(w2)
        else:
            print('Lo sentimos, la palabra no es válida')
            played_words.append(w1)
            played_words.append(w2)
    return played_words
played_words=palabras_encadenadas(w1, w2)
print(f'Las palabras jugadas fueron:', palabras_encadenadas(w1, w2))

# Parte II-b: ¡Ayuda a Pyratilla a comprobar si alguna de las palabras
# en played_words supera las 7 letras utilizando funciones lambda y 
# alguna de las funciones vistas en la sección 11.

print('La logitud de las palabras ingresadas son:')
aux=reduce(lambda x,y: (len(x), len(y)), played_words)
print(aux)
aux=list(filter(lambda x: x>7, aux))
print(f' El número de caracter mayor que 7 es:  {aux} ')
# Parte II-c:  Ayuda a Pyratilla a eliminar Isla Torvaa de unvisited_islands y 
# añadirla al conjunto visited_islands de la entrada 08 de su diario.
print('-------------------Llegada a la Isla Torvaa---------------------')
print('Navegante Pyerce, muestre la lista de todas las Islas pendientes por visitar') 
islands=set(['Golosa','Arrecife','Lejana','Torva','Verde'])
print(islands)
print('\n Borren la Isla Torva, que ya estamos desembarcando, muestre la lista de Islas visitadas')
visited_islands=set(['Alegre','Arrecife','Espesura','Torva' ]) 
unvisited_islands=islands.difference(visited_islands) 
print(f'Lista de Islas visitadas: {visited_islands}\n')