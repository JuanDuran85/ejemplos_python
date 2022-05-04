"""_summary_

    Funciones anidadas: es una funcion que se puede llamar dentro de otra funcion.
    No sepuede usar la funcion interna anidada desde fuera la funcion externa.

"""

# funciones anidadas

def calculadora(a,b, opera = "sumar"):
    #funcion anidada
    def sumar(a,b):
        return a+b
    
    def restar(a,b):
        return a-b
    
    def multiplicar(a,b):
        return a*b
    
    def dividir(a,b):
        return a/b
    
    operaciones = {
        "sumar": sumar,
        "restar": restar,
        "multiplicar": multiplicar,
        "dividir": dividir
    }
    
    # se llama a la funcion anidada
    print(f"El resultado de {opera} es: {operaciones[opera](a,b)}")

calculadora(1,2,"dividir")


# ---------------------------------------------------------------------------------------------
# funcion aniada
def mostrar(texto: str) -> str:
    def minusculas(entrada_texto: str) -> str:
        return entrada_texto.lower()
    return minusculas(texto)

print(mostrar("Mensaje Para Funcion Anidada..."))

# ---------------------------------------------------------------------------------------------
# retornando una funcion anidada para poder ser utilizada externamente

def hablar(volumen: float):
    def mayusculas(texto: str) -> str:
        return texto.upper()
    def minusculas(texto: str) -> str:
        return texto.lower()
    if volumen < 0.7:
        return minusculas
    else:
        return mayusculas
    
print(hablar(0.5)("Mensaje A poco Volumen"))
print(hablar(0.95)("Mensaje A mucho Volumen"))
variable_funcion = hablar(0.95)
print(variable_funcion("Mensaje A mucho Volumen"))
