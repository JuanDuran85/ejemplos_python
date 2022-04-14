"""_summary_

    Juego de Cartas con POO

"""

class Interfaz:
    def solicitar_numero_real(self, titulo: str) -> float:
        variable: str = input(titulo)
        try:
            variable_numerica: float = float(variable)
        except ValueError:
            print("El dato ingresado no es un numero")
            variable_numerica = 0
        return variable_numerica
    
    def solicitar_numero_entero(self, titulo: str) -> int:
        variable: str = input(titulo)
        try:
            variable_numerica: int = int(variable)
        except ValueError:
            print("El dato ingresado no es un numero")
            variable_numerica = 0
        return variable_numerica
    
if __name__ == '__main__':
    interfaz: Interfaz = Interfaz()
    numero_real = interfaz.solicitar_numero_real("Ingresa un numero real: ")
    print(f"El numero ingresado es: {numero_real}")
    numero_entero = interfaz.solicitar_numero_entero("Ingresa un numero entero: ")
    print(f"El numero ingresado es: {numero_entero}")
    