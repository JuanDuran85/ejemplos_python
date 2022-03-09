"""_summary_

Utilizando generasores con exceptions para capturar el final del generador

"""

from typing import Generator

def squeres(count: int) -> Generator[int, None, None]:
    total: int = 0
    for n in range(count):
        value: int = n ** 2
        total += value
        yield value
    return total

try:
    iter_squeres: Generator[int, None, None] = squeres(10)
    while True:
        print(next(iter_squeres))
except StopIteration as e:
    print(f"Total= {e.value}")