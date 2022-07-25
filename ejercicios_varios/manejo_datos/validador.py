def validate(opciones: list, eleccion: str) -> str:
    """_summary_
    Funcion para validar una eleccion de usuario en una lista de validaciones
    Args:
        opciones (list): Las opciones con las que se desea comparar
        eleccion (str): La eleccion del usuario

    Returns:
        str or None: retorna la eleccion del usuario si se encuentra dentro de las opciones o None si no se encuentra
    """
    while eleccion not in opciones:
        eleccion: str = input("Opción no válida, ingrese una de las opciones válidas: ").lower()
    return eleccion

if __name__ == "__main__":
    
    letras: list = ["a","b","c","d"]
    eleccion: str = input("Ingresa una Opción: ").lower()
    
    while validate(letras, eleccion) is None:
        eleccion: str = input("Opción no válida, ingrese una de las opciones válidas: ").lower()
        
    print(f"Has elegido la opción: {eleccion}")