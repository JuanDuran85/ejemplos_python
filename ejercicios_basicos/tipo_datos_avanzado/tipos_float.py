# numeros del tipo float
numero = 4.74656
print(numero)
print(type(numero))
print(f"numero: {numero:.2f}")

# trabajando con el constructor float
numero = float(4.74656)
print(f"numero: {numero:.2f}")
numero = float(345)
print(f"numero: {numero}")
print(f"numero: {numero:.2f}")
numero = float('97')
print(f"numero: {numero}")
print(f"numero: {numero:.4f}")

# usando notacion cientifica "exponencial"
numero = 447.4656564334e-6
print(f"numero: {numero}")
print(f"numero: {numero:.2f}")
print(f"numero: {numero:.2e}")

# cualquier calculo que incluya un float, se promueve a float
numero = 4.74656 + 2
print(f"numero: {numero}")
