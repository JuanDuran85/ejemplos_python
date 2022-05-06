"""_summary_

    Using functools library
    Using reduce function

"""

from functools import reduce

print('-----------------------------------------------------------')
# Print Fibonacci Sequence Upto N Terms: A Fibonacci sequence is a series of numbers where each term is the sum of the two preceding ones, starting from 0 and 1. You can print the Fibonacci series up to n terms using the lambda function.

fibonacci_sequence = lambda num: reduce(lambda x, _: x+[x[-1]+x[-2]], range(num-2),[0,1])
print(f"{fibonacci_sequence(10) = }")
print(f"{fibonacci_sequence(5) = }")

print('-----------------------------------------------------------')
# Con la función reduce() y una funcion lambda, retornar la suma de una lista de números:
number_list: list = [4,7,2,8,4,1,8,9,3,-6,-9]
print(f"{number_list = }")
total_sum: int = int(reduce(lambda value, result: result + value, number_list))
print(f"{total_sum = }")
print('-----------------------------------------------------------')