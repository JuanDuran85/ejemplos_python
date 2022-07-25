import preguntas as preguntas_total
from print_preguntas import print_pregunta

def verificar(alternativas: list, eleccion: str) -> bool:
    """_summary_
        Funcion encargada de verificar si la alternativa elegida por el usuario es correcta
    Args:
        alternativas (list): Lista de alternativas de la pregunta disponible 
        eleccion (str): Eleccion de usuario

    Returns:
        bool: Retorna true o false dependiendo si es correcta o no la eleccion del usuario
    """
    eleccion = ['a', 'b', 'c','d'].index(eleccion)
    if (alternativas[eleccion][1] == 1):
        return True
    return False


if __name__ == '__main__':
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = preguntas_total.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'][0],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    print(verificar(pregunta['alternativas'], respuesta))






