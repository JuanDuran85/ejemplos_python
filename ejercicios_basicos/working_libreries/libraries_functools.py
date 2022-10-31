"""_summary_

    Using functools library
    Using reduce function
    Using singledispatch

"""

from functools import reduce, singledispatch

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

print('-----------------------------------------------------------')
#----------------------------------------------------------------------------------------------
# singledispatch
#----------------------------------------------------------------------------------------------
'''
If you want to transform a function into a single-dispatch generic function.

To define a generic function, decorate it with the @singledispatch decorator. When defining a function using @singledispatch
'''
@singledispatch
def add_func(a,b):
    raise NotImplementedError('Unsupported type')

@add_func.register(int)
def _(a,b):
    print(f"First argument is type: {type(a)}")
    print(f"Second argument is type: {type(b)}")
    print(f"Sum: {a+b}")
    
    
@add_func.register(str)
def _(a,b):
    print(f"First argument is type: {type(a)}")
    print(f"Second argument is type: {type(b)}")
    print(f"Sum: {a+b}")
    
@add_func.register(list)
def _(a,b):
    print(f"First argument is type: {type(a)}")
    print(f"Second argument is type: {type(b)}")
    print(f"Sum: {a+b}")
    
add_func(1,2)
add_func('Python','functools')
add_func([1,2,3],[4,5,6])

print('-----------------------------------------------------------')
