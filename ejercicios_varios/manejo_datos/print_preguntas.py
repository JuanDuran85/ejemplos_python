import preguntas as preguntas_total

def print_pregunta(enunciado: str, alternativas: list) -> None:
    """_summary_
        Funcion encarda de mostrar por pantalla el enunciado y las alternativas de la pregunta a responder por parte del usuario.
    Args:
        enunciado (str): El enunciado de la pregunta
        alternativas (list): La lista de alternativas de la pregunta
    """
    print(f'''
          {enunciado}:
          A. {alternativas[0][0]}
          B. {alternativas[1][0]}
          C. {alternativas[2][0]}
          D. {alternativas[3][0]}
          ''')
    
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = preguntas_total.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'][0],pregunta['alternativas'])