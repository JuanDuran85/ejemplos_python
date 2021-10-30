# trabajando con NaN
# NaN no es sensible a mayusculas o minusculas
import math
from decimal import Decimal

print("".center(50, "-"))
numero = float('NaN')
print(f"Numero: {numero}")
print(type(numero))
print(f"Es un NaN: {math.isnan(numero)}")
print("".center(50, "-"))

# trabajando con la linreria Decimal
numero_2 = Decimal('NaN')
print(f"Numero: {numero_2}")
print(type(numero_2))
print(f"Es un NaN: {math.isnan(numero_2)}")
print("".center(50, "-"))