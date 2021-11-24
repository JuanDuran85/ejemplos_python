# alcance de una variable (scope)

variable_global = "Valor de la variable global"

def main():
    # para modificar una variable global dentro de una función, se debe usar la palabra reservada global al inicio de la funcion
    global variable_global
    variable_local = "Valor de la variable local"
    print(f"Llamando a la variable global desde la funcion: {variable_global}")
    print(F"Valor de la varibale local: {variable_local}")
    variable_global = "Nuevo valor de la variable global dentro de la funcion"
    # anidando funcion
    def new_funcion():
        print(f"Llamando a la variable global desde la funcion anidada: {variable_global}")
        print(F"Valor de la varibale local desde la funcion anidada: {variable_local}")
        
    new_funcion()

print(f"Llamando a la variable global fuera la funcion: {variable_global}")
main()


def funcion_externa():
    varibale_local_funcion_externa = "Valor de la varible local externa dentro de la funcion"

    def funcion_interna():
        # el nonlocal se usa para poder modificar una varible interna de la funcion padre dentro de la funcion anidada
        nonlocal varibale_local_funcion_externa
        print(f"Valor de la varibale: {varibale_local_funcion_externa}")
        varibale_local_funcion_externa = "Nuevo valor de la varibale local externa dentro de la funcion anidada"
        print(f"Nuevo valor de la varibale: {varibale_local_funcion_externa}")
        
    funcion_interna()
    
funcion_externa()

# ----------------------------------------------------------------------
# ejemplo con funciones y scope de una varibale

contador = 0

def mostrar_contador():
    print(f"Valor de la variable contador: {contador}")
    
def incrementar_contador():
    global contador
    contador += 1
    
mostrar_contador()
incrementar_contador()
mostrar_contador()
incrementar_contador()
mostrar_contador()