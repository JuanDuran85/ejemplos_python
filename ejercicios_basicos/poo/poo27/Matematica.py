"""_summary_
    Ejercicio estructuras de repetición: coseno.
    
    Implemente un método que sea capaz de calcular el coseno de x. El método deberá recibir los valores de: x y n y retornar el resultado de la operación. Debe asegurarse que el valor de n sea un número entero positivo. Deberá realizar todas las operaciones correspondientes a x^n. Si el número recibido es impar, deberá utilizar el siguiente número par hacia arriba inclusive en la serie.
    
    Para realizar el cálculo, considere la siguiente serie:
    - cos x = 1 - x^2/2! + x^4/4! - x^6/6! + ...
    
    - Implemente un método que sea capaz de calcular el coseno de x. 
    - El método deberá recibir los valores de: x y n y retornar el resultado de la operación. 
    - Debe asegurarse que el valor de n sea un número entero natural (comenzando en 0 en adelante). 
    - Deberá realizar todas las operaciones correspondientes a x[n]
    - Si el número recibido es impar, deberá utilizar el siguiente número par hacia arriba inclusive en la serie. 
    
    Cabe resaltar como aclaración que si se recibe un valor de 2 para x y de 5 para n se debe:

    - Convertir el valor de n al siguiente par que sería 6 
    - Realizar las sumas de fracciones: 1 - 2^2/2! + 2^4/4! - 2^6/6!
    - Retornar el resultado de esa operación
    - Note como parte de su diseño que los signos de suma y resta van intercalados

"""

class Matematicas:
    def calcular_coseno(self, x: int,n: int) -> float:
        # Implemente aquí su solución y retorne el resultado
        if n >= 0:
            if n % 2 != 0:
                n += 1
                return self.__calculo_final_coseno(x,n)
            else:
                return self.__calculo_final_coseno(x,n)
        else:
            return 0
            
    def __calculo_final_coseno(self,x:int, n: int) -> float:
        lista_valores: list = []
        signo: int = 1
        for i in range(0,n+1,2):
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
    print(calculo_uno.calcular_coseno(5,6))