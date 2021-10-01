datos = (2,4,6,32,2,67);
print("datos 1,3,5")
print(datos[1]);
print(datos[3]);
print(datos[5]);

print("Todos los datos");
for i in range(0,len(datos)):
    print(datos[i]);

print("Todos los datos al reves");
for i in range(len(datos)-1,-1,-1):
    print(datos[i]);

libro1 = {
    "autor": "XYZ",
    "titulo": "ABC",
    "paginas": 123,
}

print("libro 1: ", libro1);
print("Autor: ", libro1["autor"]);

#ejemplos con tuplas
print("Ejemplo con tuplas");
n1 = 0;
semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo");

while n1 < 1 or n1 > 7:
    n1 = int(input("Ingresa un numero entero entre el 1 y el 7: "));

print("El dia de la semana es: ",semana[n1-1]);

print("Ejemplo con tuplas 2");
n1 = 0;
semana = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre");

while n1 < 1 or n1 > 12:
    n1 = int(input("Ingresa un numero entero entre el 1 y el 12: "));

print("El mes del año es: ",semana[n1-1]);

# ejemplo con diccionarios

meses = {
    "enero": 31,
    "febrero": 28,
    "marzo": 31,
    "abril": 30,
    "mayo": 31,
    "junio": 30,
    "julio": 31,
    "agosto": 31,
    "septiembre": 30,
    "octubre": 31,
    "noviembre": 30,
    "diciembre": 31,
}

mes = input("Ingresa el nombre del mes a buscar: ");
print("El mes ingresado: " + mes.lower() + ", tiene " + str(meses[mes]) + " dias");