"""_summary_

    Implementado la libreria Math

"""

# trabajando con la libereria math

import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pow(2,3))
print(math.pi)
print(math.e)
print(math.sin(math.pi) / 2)
print(math.cos(math.pi) / 2)
print(math.tan(math.pi) / 4)
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
print(math.degrees(math.pi))
print(math.radians(180))
print(math.fabs(-1))
print(math.ceil(1.2))
print(math.floor(1.2))
print(math.trunc(1.2))
print(math.exp(1))
print(math.log(1))
print(math.log10(1))
print(math.log2(1))
print(math.log1p(1))
print(math.expm1(1))
print(math.erf(1))
print(math.erfc(1))
print(math.gamma(1))
print(math.lgamma(1))
print(math.isfinite(1))
print(math.isinf(1))
print(math.isnan(1))
print(math.isclose(1,1))
print(math.copysign(1,1))
print(math.fmod(1,1))
print(math.frexp(1))
print(math.ldexp(1,1))
print(math.modf(1))
print(math.gcd(1,1))
print(math.isqrt(1))


float_list = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
print(sum(float_list))
print(math.fsum(float_list)) # da mas exacto


# ------------------------------------------------------------------------------------------------

'''
No uses '==' para comprobar si dos puntos flotantes son iguales. Especialmente después de realizar algunas operaciones aritméticas. Usa math.isclose() en su lugar.
'''
# por ejemplo, la suma a continuacion no es exacta gracias al error de redondedo de los decimales
a: float = 0.1 + 0.2
print(f"{a = }")
# para verificar el error por igualdad
print(f"{a == 0.3}") # el resultado es False
# Por consiguiente se recomienda implementar la funcion "math.isclose()" de la libreria math
print(f"{math.isclose(a, 0.3)}") # el resultado es True


'''
    Use math.fsum() to accurately sum the numbers
'''
# por ejemplo
nums: list = [0.1119] * 10
print(f"{nums = }")
print(f"{sum(nums) = }")
print(f"{math.fsum(nums) = }")


'''
    Use math.sqrt() to calculate the square root of a number. But, you can use other tricks to calculate the square root.
'''
# with math.sqrt()
print(f"{math.sqrt(25) = }")
# with **
print(f"{ 25 ** 0.5 = }")
# with pow
print(f"{ pow(25,0.5) = }")