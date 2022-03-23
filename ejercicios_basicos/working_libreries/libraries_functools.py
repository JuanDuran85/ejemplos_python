"""_summary_

    Using functools library

"""

from functools import reduce

# Print Fibonacci Sequence Upto N Terms: A Fibonacci sequence is a series of numbers where each term is the sum of the two preceding ones, starting from 0 and 1. You can print the Fibonacci series up to n terms using the lambda function.

fibonacci_sequence = lambda num: reduce(lambda x, _: x+[x[-1]+x[-2]], range(num-2),[0,1])
print(f"{fibonacci_sequence(10) = }")
print(f"{fibonacci_sequence(5) = }")