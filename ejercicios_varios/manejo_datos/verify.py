import preguntas as preguntas_total
from print_preguntas import print_pregunta

def verificar(alternativas: list, eleccion: str) -> bool:
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






