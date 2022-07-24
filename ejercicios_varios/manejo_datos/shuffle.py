import preguntas as preguntas_total
import random

def shuffle_alt(pregunta_entrada):
    random.shuffle(pregunta_entrada['alternativas'])
    return pregunta_entrada['alternativas']

if __name__ == '__main__':
    print(preguntas_total.pool_preguntas['basicas']['pregunta_1'])
    shuffle_alt(preguntas_total.pool_preguntas['basicas']['pregunta_1'])
    print(preguntas_total.pool_preguntas['basicas']['pregunta_1'])