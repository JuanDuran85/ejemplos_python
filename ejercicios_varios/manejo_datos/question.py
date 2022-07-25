import preguntas as preguntas_total
import random
from shuffle import shuffle_alt

opciones: dict = {
    'basicas': [1,2,3],
    'intermedias': [1,2,3],
    'avanzadas': [1,2,3]
}

def choose_q(dificultad: str) -> str and list:
    """_summary_
        Funcion encarga de retornar la el enunciado y la lista de alternativas para la pregunta, dependendiendo del nivel de dificultad
    Args:
        dificultad (str): Dificultad de la pregunta

    Returns:
        str and list: retorna el enunciado y la lista de alternativas de la pregunta
    """
    preguntas: dict = preguntas_total.pool_preguntas.get(dificultad)
    
    global opciones
    n_elegido: int = opciones.get(dificultad)[random.randint(0, len(opciones[dificultad])-1)]
    opciones[dificultad].remove(n_elegido)
    
    pregunta: dict = preguntas[f'pregunta_{n_elegido}']
    alternativas: list = shuffle_alt(preguntas[f'pregunta_{n_elegido}'])
    
    return pregunta['enunciado'][0], alternativas

if __name__ == '__main__':
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')