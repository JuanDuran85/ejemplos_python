# trabajando con valores infinitos
import math
from decimal import Decimal

numero_infinito = float('inf')
print(numero_infinito)
print(type(numero_infinito))

print(f"Es infinito? {math.isinf(numero_infinito)}")

numero_infinito = float('-inf')
print(numero_infinito)
print(type(numero_infinito))

print(f"Es infinito? {math.isinf(numero_infinito)}")

# trabajando con el modulo math

numero = math.inf
print(numero)
print(type(numero))
print(f"Es infinito? {math.isinf(numero)}")

# trabajando con el modulo Decimal
print("\n".center(50, "-"))
otro_numero = Decimal('Infinity')
print(otro_numero)
print(type(otro_numero))
print(f"Es infinito? {math.isinf(otro_numero)}")