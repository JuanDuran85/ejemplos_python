# trabajando con valores infinitos
import math

numero_infinito = float('inf')
print(numero_infinito)
print(type(numero_infinito))

print(f"Es infinito? {math.isinf(numero_infinito)}")

numero_infinito = float('-inf')
print(numero_infinito)
print(type(numero_infinito))

print(f"Es infinito? {math.isinf(numero_infinito)}")