# implementando set
# un set es una coleccion de elementos unicos y es mutable
# los elementos de un set deben ser inmutables

conjunto = {("valores",12, True),23,False}
print(conjunto)

# para generar un set vacio se utilia el construtor de set
vacio_set = set()
print(vacio_set)
print(type(vacio_set))
# agregando elementos a un set
vacio_set.add(23)
vacio_set.add(True)
vacio_set.add((7,"valor"))
print(vacio_set)
# conviertiendo un lista a un set para eliminar valores duplicados
lista_1 = [-3,-5,3,6,-7,3,-3,56,-7,3,7]
lista_2 = set(lista_1)
print(lista_2)
# agregando elementos a un set desde otro set
set_2 = {1,2,3,4,5,6,7,8,9,10}
lista_2.update(set_2)
print(lista_2)

# copiar un set (copia poco profunda, solo copia la referencia)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# verificar el contenido
print(f"El contenido es igual: {conjunto == conjunto_copia}")
# verificar la referencia de los elementos
print(f"Es la misma referencia: {conjunto is conjunto_copia}")

# operaciones de conjuntos utilizando set
# personas con distintas caracteristicas
pelo_negro = {"Juan","Jose","Maria"}
pelo_amarillo = {"Karla", "Mariana", "Desiree"}
ojos_cafe = {"Jose", "Mariana"}
menores_30 = {"Mariana","Juan","Jose"}

# todos con ojos cafe y pelo rubio (union) (no se repiten los elementos)
print(f"Personas con ojos cafe y pelo rubio: {ojos_cafe.union(pelo_amarillo)}")

# Invertir el orden con el mismo resultado (conmutativa)
print(ojos_cafe.union(pelo_amarillo))