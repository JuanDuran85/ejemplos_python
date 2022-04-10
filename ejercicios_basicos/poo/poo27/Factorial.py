"""_summary_

    Factorial con clases y funciones recursivas

"""

class Recursividad:
    
    def calcular_factorial(self, n: int) -> int or None:
        if n == 0:
            return 1
        elif n <= -1:
            return None
        else:
            return n * self.calcular_factorial(n-1)
        
factorial_uno: Recursividad = Recursividad()
print(f"{factorial_uno.calcular_factorial(-10) = } ")