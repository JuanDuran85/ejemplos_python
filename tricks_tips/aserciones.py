"""_summary_

    Aplicando aserciones en python para manejo de errores
    
    las aserciones pueden ayudar a depurar el programa de errores, arrojando una AssertionError

"""

# Division entre cero
def division_zero(a:int, b:int) -> int:
    # se asegura que el valor de b no sea cero para poder continuar
    assert b != 0, 'Division entre cero'
    return (a/b)

if __name__ == '__main__':
    print(division_zero(10,3))
    print(division_zero(34,7))
    print(division_zero(10,0))