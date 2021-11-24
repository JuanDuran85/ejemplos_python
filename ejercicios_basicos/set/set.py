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
pelo_negro = {"Juan","Jose","Maria", "Mariana"}
pelo_amarillo = {"Karla", "Petra", "Desiree"}
ojos_cafe = {"Jose", "Mariana"}
menores_30 = {"Mariana","Juan","Jose"}

# todos con ojos cafe y pelo rubio (union) (no se repiten los elementos)
print(f"Personas con ojos cafe y pelo rubio: {ojos_cafe.union(pelo_amarillo)}")

# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_amarillo.union(ojos_cafe))

# (interseccion) (no se repiten los elementos) solo las personas con ojos cafe y pelos rubio. Es una operacion conmutativa
print(f"Personas con ojos cafe y pelo rubio: {ojos_cafe.intersection(pelo_amarillo)}")

# (diferencia) Pelo negro pero sin ojos cafe - operacion no conmutativa
# personas que se encuentran en el primer set pero no en segundo
print(pelo_negro.difference(ojos_cafe))

# diferencia simetrica - Personas con pelo negro u ojos cafe pero no ambos. Operacion conmitativa
print(pelo_negro.symmetric_difference(ojos_cafe))

# preguntas con set
# preguntar si un set esta contenido en otro (subset)
# revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))


# preguntar si un set contiene a otro set
# Revisar si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issuperset(pelo_negro))

# pregunta si los de pelo negro no tienen pelo rubio (distjoin)
print(pelo_negro.isdisjoint(pelo_amarillo))