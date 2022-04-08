"""_summary_

    Implemente un método que sea capaz de calcular el seno de x. El método deberá recibir los valores de: x y n y retornar el resultado de la operación. 

    Debe asegurarse que el valor de n sea un número entero positivo y 
    
    realizar todas las operaciones correspondientes a [X]^[N]
    
    Si el número recibido es par, deberá utilizar el siguiente número impar hacia arriba inclusive en la serie.
    
"""

class Matematicas:
    
    def calcular_seno(self,x: int,n: int) -> float:
        if n >= 0:
            if n % 2 == 0:
                n += 1
                return self.__calculo_final_coseno(x,n)
            else:
                return self.__calculo_final_coseno(x,n)
        else:
            return 0
        
    def __calculo_final_coseno(self,x: int, n: int) -> float:
        lista_valores: list = []
        signo: int = -1
        lista_valores.append(x)
        for i in range(3,n+1,2):
            lista_valores.append((signo)*((x**i)/(self.__factorial_numero(i))))
            signo *= -1
            print(f"{lista_valores = }")
        return sum(lista_valores)
    
    def __factorial_numero(self, num: int) -> int:
        if num == 0:
            return 1
        else:
            return num * self.__factorial_numero(num-1)

if __name__ == '__main__':
    calculo_uno: Matematicas = Matematicas()
    print(calculo_uno.calcular_seno(2,5))        