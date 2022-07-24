import preguntas as preguntas_total
import random
from shuffle import shuffle_alt

opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}

def choose_q(dificultad):
    preguntas = preguntas_total.pool_preguntas[dificultad]
    
    global opciones
    n_elegido = opciones.get(dificultad)[random.randint(0, len(opciones[dificultad])-1)]
    opciones[dificultad].remove(n_elegido)
    
    pregunta = preguntas[f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(preguntas[f'pregunta_{n_elegido}'])
    
    return pregunta['enunciado'], alternativas

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