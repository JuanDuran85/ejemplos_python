def validate(opciones, eleccion):
    if eleccion in opciones:
        return eleccion
    return None

if __name__ == "__main__":
    
    letras = ["a","b","c","d"]
    eleccion = input("Ingresa una Opción: ").lower()
    
    while validate(letras, eleccion) is None:
        eleccion = input("Opción no válida, ingrese una de las opciones válidas: ").lower()
        
    print(f"Has elegido la opción: {eleccion}")