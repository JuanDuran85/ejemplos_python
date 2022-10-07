"""_summary_

    Aplicando aserciones en python para manejo de errores
    
    las aserciones pueden ayudar a depurar el programa de errores, arrojando una AssertionError

"""

# Division entre cero
def division_zero(a:int, b:int) -> float:
    # se asegura que el valor de b no sea cero para poder continuar
    assert b != 0, 'Division entre cero'
    return (a/b)

def calculo_promedio(calificaciones: list) -> None:
    assert calificaciones, 'Debe existir calificaciones'
    print(f"El promedio de calificaciones es: {sum(calificaciones)/len(calificaciones)}")
    
def aplicar_descuento(producto: dict,descuento: float) -> None:
    descuento_total: float = producto['precio'] - (producto['precio'] * (descuento / 100))
    print(f"Nuevo precio del producto: {descuento_total}")
    assert 0<= descuento_total <= producto['precio'], f"El nuevo precio {descuento_total}, no es permitido"

if __name__ == '__main__':
    print(division_zero(10,3))
    calificaciones = [4,6,8,5,7,9]
    calculo_promedio(calificaciones)
    producto: dict = {
        'nombre':'Teclado',
        'precio': 1500.00
    }
    aplicar_descuento(producto,10)