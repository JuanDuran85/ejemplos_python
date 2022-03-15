"""_sumary_:

    Usando la libreria itertools
    Using itertools library
    Using zip_longest
    Using count
    Using permutations
    Using product
    Using starmap

"""

from itertools import accumulate, filterfalse, zip_longest, count, permutations, product, starmap, chain, repeat, cycle
from typing import Generator, Iterable

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using lists - Can be: ordered, mutable, duplicates'''
print("\n Using lists with itertools \n")

n_values_in_list_two = range(0,10,2)
print(f"{n_values_in_list_two = }")

# With accumulate from itertools librery, you can sum the values ​​in a list
print(f"{list(accumulate(n_values_in_list_two)) = }")


# The filterfalse function creates a iterator that filters elements from iterable returning only those for which the predicate is False 
list_any: list = [None, True, 1, 0, False, '', [], {}, [1,2], {'a':1}, 'string...']
list_filter: list = list(filterfalse(bool, list_any))
print(f"{list_filter = }")


# If you want to zip uneven list in Python, you can either accept that one list will be truncated ot you can use zip_longest from itertools library

x: list = [1, 2, 3, 4, 5]
y: list = ['a', 'b', 'c']

result_x_y: list = list(zip_longest(x, y))
print(f"{result_x_y = }")

# Make an iterator that returns evenly spaced values starting with number start --> itertools.count(start=0, step=1)
# default sequence, start at 0 and count by one
sequence: count = count()
print(f"{next(sequence) = }")
print(f"{next(sequence) = }")
# sequence with inital value
sequence_two: count = count(10)
print(f"{next(sequence_two) = }")
print(f"{next(sequence_two) = }")
print(f"{next(sequence_two) = }")
# sequence with inital value and step
sequence_three: count = count(100, 10)
print(f"{next(sequence_three) = }")
print(f"{next(sequence_three) = }")
print(f"{next(sequence_three) = }")

# If you need to create a permutation of numbers, you can use the permutation itertools library
for p in permutations([5,6,7]):
    print(''.join(str(x) for x in p))


# -------------------------------------------------------------
# Using starmap to return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence.
args_base_pow: list = [(2,3), (2,4), (2,5)]

result_pow: list = list(starmap(pow, args_base_pow))
print(f"{result_pow = }")

#--------------------------------------------------------------
# 
def alpha_iter(start: str, end: str) -> Iterable[str]:
    """
    Generate an iterable of strings from start to end
    """
    sords: map[int] = map(ord, start)
    eords: map[int] = map(ord, end)
    ranges: Generator[range, None, None] = (range(s,e+1) for s,e in zip(sords,eords))
    for ords in product(*ranges):
        yield ''.join(map(chr, ords))
        
print(f"{list(alpha_iter('a','z')) = }")

# ---------------------------------------------------------------------------------------------
# infinity sequence of numbers with chain, repeat and cycle
sequ = chain(repeat(17,4), cycle(range(4)))
for i,num in enumerate(sequ):
    print(f"{i} - {num}")
    if i == 30:
        break



