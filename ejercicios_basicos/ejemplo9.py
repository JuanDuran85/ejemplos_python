x = 2;
y = 3;
print(x + y);
print(x - y);
print(x * y);
print(x / y);
print(x % y);
print(x ** y);

print("Direccion de memoria de x");
print(id(x));
print("Direccion de memoria de y");
print(id(y));

print("Tipo de datos con type")
print("El ':str' se utiliza para dar un pista del posible valor que deberia contener una varibale")
cadena: str = "Cadena de string"
boleano = False
print(type(cadena))
print(type (x))
print(type(boleano))

# Area de un rectangulo

alto = int(input("Ingrese el alto: "))
ancho = int(input("Ingrese el ancho: "))
area = alto * ancho
print("El area del rectangulo es: ", area)
perimetro = 2 * (alto + ancho)
print('El perimetro del \'rectangulo\' es: ', perimetro)


# Determinar cual es el mayor de dos numeros ingresados por el usuario

numero_uno = int(input("Ingrese un numero A: "))
numero_dos = int(input("Ingrese un numero B: "))

if numero_uno > numero_dos:
    print(f"{numero_uno} es mayor que {numero_dos}. Por lo tanto, el numero mayor es: {numero_uno}")
elif numero_dos > numero_uno:
    print(f"{numero_dos} es mayor que {numero_uno}. Por lo tanto, el numero mayor es: {numero_dos}")
else:
    print("Los numeros ingresados son iguales")

    