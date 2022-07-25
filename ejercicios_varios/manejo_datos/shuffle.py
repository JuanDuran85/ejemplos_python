import preguntas as preguntas_total
import random

def shuffle_alt(pregunta_entrada: dict) -> list:
    """_summary_
    Funcion encargada de barajar las alternativas de una pregunta
    Args:
        pregunta_entrada (dict): Recibe el diccionario donde se encuentra el eneunciado y las alternativas

    Returns:
        list: retorna las alternativas barajadas en forma de lista
    """
    random.shuffle(pregunta_entrada['alternativas'])
    return pregunta_entrada['alternativas']

if __name__ == '__main__':
    print(preguntas_total.pool_preguntas['basicas']['pregunta_1'])
    shuffle_alt(preguntas_total.pool_preguntas['basicas']['pregunta_1'])
    print(preguntas_total.pool_preguntas['basicas']['pregunta_1'])