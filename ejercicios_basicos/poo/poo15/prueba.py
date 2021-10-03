from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora
from Orden import Orden

monitor1 = Monitor("HP", 22)
monitor2 = Monitor("LG", 24)
teclado1 = Teclado("HP", "USB")
teclado2 = Teclado("Dell", "USB")
raton1 = Raton("HP", "USB")
raton2 = Raton("Dell", "USB")
monitores = [monitor1, monitor2]
teclados = [teclado1, teclado2]
ratones = [raton1, raton2]

computadora_1 = Computadora("Computadora 1", monitores, teclados, ratones)
#print(computadora_1)
computadora_2 = Computadora("Computadora 2", monitores, teclados, ratones)
#print(computadora_2)

ordenes = [computadora_1, computadora_2]
orden_1 = Orden(ordenes)
print(orden_1)

ordenes = [computadora_1, computadora_2]
orden_2 = Orden(ordenes)
print(orden_2)