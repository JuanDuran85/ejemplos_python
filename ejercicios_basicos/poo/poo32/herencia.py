"""_summary_

    Herencia en POO bajo metodología DRY (Dont Repeat Yourself)

"""

class Poligonos:
    
    def __init__(self, cantidad_lados: int) -> None:
        self.cantidad_lados = cantidad_lados
        
    def solicitar_lados(self) -> None:
        self.lados: list = [float(input(f"Ingresa el lado {str(i+1)}: ")) for i in range(self.cantidad_lados)]
        
class Rectangulo(Poligonos):
    
    def calcular_perimetro(self) -> float:
        # se puede desestructurar con: a,b,c,d = self.lados
        # o aplicando la funcion sum para que sume todos los valores de la lista
        return sum(self.lados)
    
    def calcular_area(self) -> float:
        largo, ancho = self.lados
        return largo * ancho
    
class Cuadrado(Poligonos):
        
    def calcular_area(self) -> float:
        lado, = self.lados
        return lado ** 2
    
    
if __name__ == '__main__':
    
    rectangulo_uno: Rectangulo = Rectangulo(4)
    rectangulo_uno.solicitar_lados()
    print(rectangulo_uno.calcular_perimetro())
    
    cuadrado_uno: Cuadrado = Cuadrado(1)
    cuadrado_uno.solicitar_lados()
    print(cuadrado_uno.calcular_area())