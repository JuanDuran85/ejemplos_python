"""_summary_

Generando un triangulo equilatero con fila de numeros

"""


def mostrar(n: int) -> None:
    x: int = 0
    for i in range(0, n):
        x += 1
        for _ in range(0, i+1):
            if x < 10:
                print(f"0{x}", end=" ")
            else:
                print(f"{x}", end=" ")
        print("\r")


n: int = int(input("Ingresa el numero de filas a mostrar: "))
mostrar(n)
