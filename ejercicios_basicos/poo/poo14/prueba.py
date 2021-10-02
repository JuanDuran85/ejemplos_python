from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(type(objeto))
    objeto.mostrar_detalle()
    # para verificar que el objeto es una instancia de la clase
    if isinstance(objeto, Gerente):
        print("El departamento es: {}".format(objeto.departamento))


empleado1 = Empleado("Ali", 3000)
imprimir_detalles(empleado1)

gerente1 = Gerente('Juan', 2000, 'Ventas')
imprimir_detalles(gerente1)



