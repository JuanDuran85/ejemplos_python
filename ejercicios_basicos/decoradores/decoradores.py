''' Un decorador recibe una funcion y retorna otra funcion. Se utiliza para extender funcionalidades '''


# 1. Funcion como decorador (a)
# 2. Funcion a decorar (b)
# 3. Funcion decorada (c)


def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print("Hola soy la funcion decorada")
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print("Adios soy la funcion decorada")
        return resultado

    return funcion_decorada_c

@funcion_decorador_a
def mostrar_mensaje():
    print("Hola desde funcion mostrar mensaje")
    
mostrar_mensaje()

@funcion_decorador_a
def sumar(a, b):
    return a + b

resultado = sumar(1, 2)
print(f'resultado suma: {resultado}')
