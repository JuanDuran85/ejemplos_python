"""_summary_

    Funciones decoradoras: son funciones que se aplican sobre otra funcion

"""

def asteriscos(funcion_a_ejecutar) -> None:
    def poner_asteriscos(*args, **kwargs) -> None:
        print("*"*30)
        funcion_a_ejecutar(*args, **kwargs)
        print("*"*30)
    return poner_asteriscos  # type: ignore

@asteriscos
def imprimir_texto(texto: str) -> None:
    print(texto.center(50, "-"))
    
imprimir_texto("Este es el texto a imprimir")