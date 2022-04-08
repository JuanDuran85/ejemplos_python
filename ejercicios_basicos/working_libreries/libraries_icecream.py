"""_summary_

    Working with library icecream
    
    ic() is like print(), but better:

    - It prints both expressions/variable names and their values.
    - It's 40% faster to type.
    - Data structures are pretty printed.
    - Output is syntax highlighted.
    - It optionally includes program context: filename, line number, and parent function.

    https://github.com/gruns/icecream

"""

from icecream import ic

def sumar(x: int, y: int) -> int:
    suma: int = x + y
    ic(x)
    ic(y)
    return suma

ic.configureOutput(prefix='[prueba] | ', includeContext=True)
ic(sumar(3,4))