# profundizando en funciones

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