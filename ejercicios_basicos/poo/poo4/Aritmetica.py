class Aritmetica:
    '''
        Docstring de la clase:
        Esta clase tiene como objetivo realizar operaciones aritméticas suma, resta, multiplicación y división.
    '''
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "No se puede dividir entre 0"

arutmetica1 = Aritmetica(13, 27)
print(f"El resultado de la suma es: {arutmetica1.sumar()}")
print(f"El resultado de la resta es: {arutmetica1.restar()}")
print(f"El resultado de la multiplicación es: {arutmetica1.multiplicar()}")
print(f"El resultado de la división es: {arutmetica1.dividir():.2f}")
