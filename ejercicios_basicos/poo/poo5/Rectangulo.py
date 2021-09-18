class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def diagonal(self):
        return (self.base ** 2 + self.altura ** 2) ** 0.5

try:
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    rectangulo1 = Rectangulo(base, altura)
    print(f"El area del rectangulo es: {rectangulo1.area()}")
    print(f"El perimetro del rectangulo es: {rectangulo1.perimetro()}")
    print(f"La diagonal del rectangulo es: {rectangulo1.diagonal():.2f}")
except ValueError:
    print("Error: El valor ingresado No es un número")