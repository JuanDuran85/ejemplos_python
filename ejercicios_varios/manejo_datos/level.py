def choose_level(n_pregunta: int, p_level: int) -> str:
    """_summary_
        Funcion encarga de retornar el nivel de la pregunta que se va a mostrar
    Args:
        n_pregunta (int): Numero de la pregunta actual
        p_level (int): Numero de preguntas por nivel

    Returns:
        str: retorna el nivel de la pregunta
    """
    if n_pregunta <= p_level:
        return "basicas"
    elif n_pregunta <= 2*p_level:
        return "intermedias"
    else:
        return "avanzadas"

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(0, 1)) 
    print(choose_level(1, 1)) 
    print(choose_level(2, 1))