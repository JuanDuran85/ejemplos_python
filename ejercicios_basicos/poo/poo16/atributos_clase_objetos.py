class Persona:
    #variable de clase
    contador_persona = 0
    
    #metodo inicializador
    def __init__(self, nombre,apellido):
        self.nombre   = nombre
        self.apellido = apellido
        
# mostrar los atributos del objeto
persona1 = Persona("Juan","Perez")
print("Nombre:",persona1.nombre)
print("Apellido:",persona1.apellido)
# para desplegar los atributos asociados a un objeto se usa el __dict__
print("Atributos del objeto:",persona1.__dict__)

# crear atributos al instante o al vuelo
print(persona1.contador_persona)
# las variables de clase no se pueden modificar desde el objeto, solo pueden ser leidas. Por lo tanto, agrega un nuevo atributo a la clase
persona1.contador_persona = 20
print(persona1.contador_persona)
print("Atributos del objeto:",persona1.__dict__)
# para acceder a la variable de clase, se debe utilizar el nombre de la clase
print(Persona.contador_persona)

#  ------------------------------------------------------------------------------------------------

''' Convertidor de temperaturas con clases '''

class ConvertidorTempratura:
    
    MAX_CELCIUS = 100
    MAX_FAHRENHEIT = 213
    
    @classmethod
    def conversor_celcius_fahrenheit(cls, temperatura):
        if temperatura > cls.MAX_CELCIUS:
            raise ValueError(f"Temperatura fuera de rango {temperatura}")
        return (temperatura * 1.8) + 32

    @classmethod
    def conversor_fahrenheit_celcius(cls, temperatura):
        if temperatura > cls.MAX_FAHRENHEIT:
            raise ValueError(f"Temperatura fuera de rango {temperatura}")
        return (temperatura - 32) / 1.8

if __name__ == '__main__':
    valor = 39
    resultado = ConvertidorTempratura.conversor_celcius_fahrenheit(valor)
    print(f"La conversion de {valor}°c a °f es: {resultado:.2f}°f")
    resultado2 = ConvertidorTempratura.conversor_fahrenheit_celcius(resultado)
    print(f"La conversion de {resultado}°f a °c es: {resultado2:.2f}°c")