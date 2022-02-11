# trabajando con funciones lambda: es una funcion anonima y pequeña (una linea de codigo)
# se usa la palabra reservada lambda, los parametros son opcionales

mi_funcion_lambda = lambda a,b: a+b
print(f"La suma es: {mi_funcion_lambda(22,53)}")

mi_funcion_lambda = lambda x: x**2
print(f"El cuadrado es: {mi_funcion_lambda(5)}")

# una funcion lambda que no recibe argumentos pero debe regresar una expresion valida
mi_funcion_lambda = lambda: "Funcion lambda sin argumentos..."
print(mi_funcion_lambda())

# asignando valores por defecto a argumentos de una variable lambda
mi_funcion_lambda = lambda a=2,b=5: a+b
print(f"La suma es: {mi_funcion_lambda()}")

mi_funcion_lambda = lambda x=2: x**2
print(f"El cuadrado es: {mi_funcion_lambda()}")

# funcion lambda copn argumentos variables *args(tuplas) y **kwargs(diccionarios)
mi_funcion_lambda = lambda *args, **kwargs: print(args, kwargs)
mi_funcion_lambda(1,5,3,2, a=5,b=34)
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(mi_funcion_lambda(1,5,3,2, a=5,b=34))

# funciones lambda con argumentos, argumentos varibales y valores por defecto
mi_funcion_lambda = lambda x,y,z=4,*args, **kwargs: x+y+z+len(args)+len(kwargs)
print(mi_funcion_lambda(1,5,3,2,5,-6, r=5,w=34))